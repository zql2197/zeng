import re
import pandas as pd
import numpy as np
import pymysql
import sqlalchemy
from pandas import DataFrame


# 不同年份上映的电影数量
from sqlalchemy import create_engine


def movie_date_publish_count(df):
    grouped = df.groupby('movie_publish_year')['movie_type'].count().reset_index()
    data = grouped.to_dict(orient='records')
    # 将数据转换成数组嵌套数组的格式
    data = [[str(i['movie_publish_year']), i['movie_type']] for i in data]
    return data


# 不同地区的电影上映数量最多的前十个地区
def movie_country_publish_top10(df):
    # 原数据中可能每个电影上映在多个地区 且不同地区之间使用逗号分隔 因此将movie_area列数据以逗号进行分隔变成列表
    series_country = df['movie_area'].str.split(',').tolist()
    # 利用set函数的特性 当数据出现重复时 只保留一个数据
    list_country = set([j for i in series_country for j in i])
    # 创建0矩阵统计不同地区电影上映的数量
    zero_list = pd.DataFrame(np.zeros((len(series_country), len(list_country))), columns=list_country)
    for i in range(len(zero_list)):
        zero_list.loc[i][series_country[i]] = 1

    # 使用聚合函数对不同地区的电影进行统计
    country_movie_counts = zero_list.sum().astype(np.int32)
    country_movie_counts = country_movie_counts.reset_index()
    country_movie_counts.columns = ['movie_area', 'count']
    # 对数据进行排序并取出数量最多的前十个地区
    country_movie_counts = country_movie_counts.sort_values(by='count', ascending=False)[:10]
    data = [[i['movie_area'], i['count']] for i in country_movie_counts.to_dict(orient='records')]
    return data


# 统计票房前十的电影
def movie_booking_top10(df):
    # 按照票房数量进行排序并取出前十的数据
    df = df.sort_values(by='movie_booking', ascending=False)
    movie_name_to_booking = df[['movie_name', 'movie_booking']][:10]
    data = [[i['movie_name'], i['movie_booking']] for i in movie_name_to_booking.to_dict(orient='records')]
    # print(data)
    return data


# 统计评分人数前十的电影
def movie_comment_top10(df):
    # 按照评论数量进行排序并取出前十的数据
    df = df.sort_values(by='movie_comments', ascending=False)
    movie_name_to_booking = df[['movie_name', 'movie_comments']][:10]
    data = [[i['movie_name'], i['movie_comments']] for i in movie_name_to_booking.to_dict(orient='records')]
    # print(data)
    return data


# 统计不同评分区间的电影数量
def movie_score_count(df):
    # 根据不同区间划分电影评分数据 区间分别为 <7.0 7.0-8.0 >8.0 三个区间
    grouped1 = df[df['movie_score'] < 7.0]['movie_score']
    grouped2 = df[(df['movie_score'] >= 7.0) & (df['movie_score'] <= 8.0)]['movie_score']
    grouped3 = df[df['movie_score'] > 8]['movie_score']
    movie_score_to_count = [{'movie_score': '<7.0', 'count': len(grouped1)},
                            {'movie_score': '7.0-8.0', 'count': len(grouped2)},
                            {'movie_score': '>8.0', 'count': len(grouped3)}]
    data = [[i['movie_score'], i['count']] for i in movie_score_to_count]
    return data


# 统计不同类型的电影数量最多的前十个类型
def movie_type_count(df):
    # 原数据中可能每个电影有多个电影类型 且不同电影类型之间使用点号分隔 因此将movie_type列数据以点号进行分隔变成列表
    series_movie_type = df['movie_type'].str.split('·').tolist()
    movie_type_list = [j for i in series_movie_type for j in i]
    # 利用set函数的特性 当数据出现重复时 只保留一个数据
    movie_type = set(movie_type_list)
    # 创建0矩阵统计不同电影类型的数量
    zero_list = pd.DataFrame(np.zeros((len(df), len(movie_type))), columns=movie_type)
    for i in range(len(df)):
        zero_list.loc[i][series_movie_type[i]] = 1

    # 使用聚合函数对不同类型的电影进行统计
    movie_type_counts = zero_list.sum().astype(int)
    movie_type_counts = movie_type_counts.reset_index()
    movie_type_counts.columns = ['movie_type', 'count']
    # 对数据进行排序并取出数量最多的前十个类型
    movie_type_counts = movie_type_counts.sort_values(by='count', ascending=False)[:10]
    data = [[i['movie_type'], i['count']] for i in movie_type_counts.to_dict(orient='records')]
    return data


if __name__ == '__main__':
    movies = pd.read_excel('movie.xlsx')
    # print(movies)
    df = pd.DataFrame(movies)
    # print(df)
    # 打印基础信息
    # print(df.info())
    # print(df.head())
    # 保留有用字段
    df = df[
        ['movie_name', 'movie_type', 'movie_area', 'movie_duration', 'movie_publish', 'movie_score', 'movie_comments',
         'movie_booking', 'movie_director']]
    # print(df)
    # 过滤数据
    # 过滤movie_type列数据
    df = df[~df['movie_type'].str.contains('类型未知')]

    # 过滤movie_area列数据
    df = df[df['movie_area'].str.contains('上映国家未知') == False]

    # 过滤movie_duration列数据
    df = df[~df['movie_duration'].str.contains('电影时长未知')]

    # 过滤movie_publish列数据
    df = df[~df['movie_publish'].str.contains('上映时间未知')]

    # 过滤movie_score列数据
    df = df[df['movie_score'].str.contains('电影评分未知') == False]

    # 过滤movie_comments列数据
    df = df[~df['movie_comments'].str.contains('评分人数未知')]

    # 过滤movie_booking列数据
    df = df[~df['movie_booking'].str.contains('电影票房未知')]

    # 过滤movie_director列数据
    df = df[~df['movie_director'].str.contains('导演未知')]

    # print(df)

    engine = create_engine("mysql+pymysql://root:root@localhost:3306/movie")
    df.to_sql(name='db_movies', con=engine, if_exists='replace')

    # 处理数据转换数据类型
    # 去掉movie_duration列数据中的分钟并将数据转换成int数据类型
    df['movie_duration'] = df['movie_duration'].apply(lambda x: int(re.findall(r'(\d+)分钟', x)[0]))

    # 将movie_score列数据转换成float类型
    df['movie_score'] = df['movie_score'].apply(lambda x: float(x))

    # 将movie_comments列数据统一单位
    df['movie_comments'] = df['movie_comments'].apply(
        lambda x: int(float(re.findall(r'(.*)万', x)[0]) * 10000) if len(re.findall(r'万', x)) > 0 else int(x))

    # 将movie_booking列数据统一单位
    df['movie_booking'] = df['movie_booking'].apply(
        lambda x: float(re.findall(r'(.*)亿', x)[0]) if len(re.findall('亿', x)) > 0 else round(
            float(x.split('万')[0]) / 10000, 2))

    # 将movie_publish转换成pandas时间类型并将数据转换成具体的年添加到pd中
    df['movie_publish'] = df['movie_publish'].apply(
        lambda x: re.findall(r'(.*)中国大陆上映', x)[0] if len(re.findall(r'中国大陆上映', x)) > 0 else x)
    df['movie_publish'] = pd.to_datetime(df['movie_publish'])
    date = pd.DatetimeIndex(df['movie_publish'])
    df['movie_publish_year'] = date.year
    # print(df)
    # 不同年份上映的电影数量
    data1 = movie_date_publish_count(df)
    # print(data1) [['年份', 数量]]

    # 不同地区的电影上映数量最多的前十个地区
    data2 = movie_country_publish_top10(df)
    # print(data2) [['地区',数量]]

    # 统计票房前十的电影
    data3 = movie_booking_top10(df)
    # print(data3) [['电影名称', 票房]]

    # 统计评论前十的电影
    data4 = movie_comment_top10(df)
    # print(data4) [['电影名称', 评论人数]]

    # 统计不同评分区间的电影数量
    data5 = movie_score_count(df)
    # print(data5) [['<7.0', 数量], ['7.0-8.0',数量], ['>8.0',数量]]

    # 统计不同类型的电影数量最多的前十个类型
    data6 = movie_type_count(df)
    # print(data6) [['类型', 数量]]

    # # 创建数据库连接
    # db = pymysql.connect(host='localhost', port=3306, user='root', passwd='root', db='movie', charset='utf8')
    # # 获取游标对象
    # with db.cursor() as cursor:
    # # 不同年份上映的电影数量
    # sql = 'insert into db_year_movie_count(year,count) values(%s,%s)'
    # try:
    #     result = cursor.executemany(sql, data1)
    #     if result:
    #         print('数据库插入数据成功')
    #         db.commit()
    #
    # except pymysql.MySQLError as error:
    #     print(error)
    #     db.rollback()
    # finally:
    #     db.close()

    # 不同地区的电影上映数量最多的前十个地区
    # sql = 'insert into db_area_movie_count(area,count) values(%s,%s)'
    # try:
    #     result = cursor.executemany(sql, data2)
    #     if result:
    #         print('数据库插入数据成功')
    #         db.commit()
    #
    # except pymysql.MySQLError as error:
    #     print(error)
    #     db.rollback()
    # finally:
    #     db.close()

    # 统计票房前十的电影
    # sql = 'insert into db_booking_movie_count(name,booking) values(%s,%s)'
    # try:
    #     result = cursor.executemany(sql, data3)
    #     if result:
    #         print('数据库插入数据成功')
    #         db.commit()
    #
    # except pymysql.MySQLError as error:
    #     print(error)
    #     db.rollback()
    # finally:
    #     db.close()

    # 统计评论前十的电影
    # sql = 'insert into db_comment_movie_count(name,comment) values(%s,%s)'
    # try:
    #     result = cursor.executemany(sql, data4)
    #     if result:
    #         print('数据库插入数据成功')
    #         db.commit()
    #
    # except pymysql.MySQLError as error:
    #     print(error)
    #     db.rollback()
    # finally:
    #     db.close()

    # 统计不同评分区间的电影数量
    # sql = 'insert into db_score_movie_count(score,count) values(%s,%s)'
    # try:
    #     result = cursor.executemany(sql, data5)
    #     if result:
    #         print('数据库插入数据成功')
    #         db.commit()
    #
    # except pymysql.MySQLError as error:
    #     print(error)
    #     db.rollback()
    # finally:
    #     db.close()

    # 统计不同类型的电影数量最多的前十个类型
    # sql = 'insert into db_type_movie_count(type,count) values(%s,%s)'
    # try:
    #     result = cursor.executemany(sql, data6)
    #     if result:
    #         print('数据库插入数据成功')
    #         db.commit()
    #
    # except pymysql.MySQLError as error:
    #     print(error)
    #     db.rollback()
    # finally:
    #     db.close()
