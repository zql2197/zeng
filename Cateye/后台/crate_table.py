import pymysql

conn = pymysql.connect(host='localhost', user='root', password='root', charset='utf8mb4')
# 创建游标
cursor = conn.cursor()
# 创建数据库的sql
sql = "CREATE DATABASE IF NOT EXISTS movie"  # new_db是要创建的数据库名字

# 执行创建数据库的sql语句
cursor.execute(sql)

# 创建电影信息的表
try:
    # 创建与数据库的连接
    # 参数分别是 指定本机 数据库用户名 数据库密码 数据库名 端口号 autocommit是是否自动提交
    db = pymysql.connect(host='localhost', user='root', password='root', database='movie', port=3306, autocommit=False)
    # 创建游标对象cursor
    cursor = db.cursor()
    # 使用execute()方法执行sql，如果表存在则删除
    cursor.execute('drop table if EXISTS db_movie_item')
    # 创建表的sql
    sql = '''
        create table db_movie_item(
        `id` int(11) NOT NULL AUTO_INCREMENT,
        `movie_name` varchar(64) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
        `movie_type` varchar(64) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
        `movie_area` varchar(64) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
        `movie_duration` varchar(64) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
        `movie_publish` varchar(64) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
        `movie_score` varchar(64) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
        `movie_comment` varchar(64) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
        `movie_booking` varchar(64) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
        `movie_director` varchar(64) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
        PRIMARY KEY (`id`) USING BTREE       
        )
    '''
    cursor.execute(sql)
    print('创建表成功')
except:
    print('创建表失败')
finally:
    # 关闭数据库连接
    conn.close()


# 创建不同年份上映的电影数量的表
# try:
#     # 创建与数据库的连接
#     # 参数分别是 指定本机 数据库用户名 数据库密码 数据库名 端口号 autocommit是是否自动提交
#     db = pymysql.connect(host='localhost', user='root', password='root', database='movie', port=3306, autocommit=False)
#     # 创建游标对象cursor
#     cursor = db.cursor()
#     # 使用execute()方法执行sql，如果表存在则删除
#     cursor.execute('drop table if EXISTS db_year_movie_count')
#     # 创建表的sql
#     sql = '''
#         create table db_year_movie_count(
#         `id` int(11) NOT NULL AUTO_INCREMENT,
#         `year` varchar(64) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
#         `count` int(11) NOT NULL,
#         PRIMARY KEY (`id`) USING BTREE
#         )
#     '''
#     cursor.execute(sql)
#     print('创建表成功')
# except:
#     print('创建表失败')
# finally:
#     # 关闭数据库连接
#     conn.close()


# 创建不同地区的电影上映数量最多的前十个地区的表
# try:
#     # 创建与数据库的连接
#     # 参数分别是 指定本机 数据库用户名 数据库密码 数据库名 端口号 autocommit是是否自动提交
#     db = pymysql.connect(host='localhost', user='root', password='root', database='movie', port=3306, autocommit=False)
#     # 创建游标对象cursor
#     cursor = db.cursor()
#     # 使用execute()方法执行sql，如果表存在则删除
#     cursor.execute('drop table if EXISTS db_area_movie_count')
#     # 创建表的sql
#     sql = '''
#         create table db_area_movie_count(
#         `id` int(11) NOT NULL AUTO_INCREMENT,
#         `area` varchar(64) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
#         `count` int(11) NOT NULL,
#         PRIMARY KEY (`id`) USING BTREE
#         )
#     '''
#     cursor.execute(sql)
#     print('创建表成功')
# except:
#     print('创建表失败')
# finally:
#     # 关闭数据库连接
#     conn.close()


# 创建统计票房前十的电影的表
# try:
#     # 创建与数据库的连接
#     # 参数分别是 指定本机 数据库用户名 数据库密码 数据库名 端口号 autocommit是是否自动提交
#     db = pymysql.connect(host='localhost', user='root', password='root', database='movie', port=3306, autocommit=False)
#     # 创建游标对象cursor
#     cursor = db.cursor()
#     # 使用execute()方法执行sql，如果表存在则删除
#     cursor.execute('drop table if EXISTS db_booking_movie_count')
#     # 创建表的sql
#     sql = '''
#         create table db_booking_movie_count(
#         `id` int(11) NOT NULL AUTO_INCREMENT,
#         `booking` float NOT NULL,
#         `name` varchar(64) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
#         PRIMARY KEY (`id`) USING BTREE
#         )
#     '''
#     cursor.execute(sql)
#     print('创建表成功')
# except:
#     print('创建表失败')
# finally:
#     # 关闭数据库连接
#     conn.close()

# 创建统计评论前十的电影的表
# try:
#     # 创建与数据库的连接
#     # 参数分别是 指定本机 数据库用户名 数据库密码 数据库名 端口号 autocommit是是否自动提交
#     db = pymysql.connect(host='localhost', user='root', password='root', database='movie', port=3306, autocommit=False)
#     # 创建游标对象cursor
#     cursor = db.cursor()
#     # 使用execute()方法执行sql，如果表存在则删除
#     cursor.execute('drop table if EXISTS db_comment_movie_count')
#     # 创建表的sql
#     sql = '''
#         create table db_comment_movie_count(
#         `id` int(11) NOT NULL AUTO_INCREMENT,
#         `name` varchar(64) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
#         `comment` bigint(20) NOT NULL,
#         PRIMARY KEY (`id`) USING BTREE
#         )
#     '''
#     cursor.execute(sql)
#     print('创建表成功')
# except:
#     print('创建表失败')
# finally:
#     # 关闭数据库连接
#     conn.close()


# 创建统计不同评分区间的电影数量的表
# try:
#     # 创建与数据库的连接
#     # 参数分别是 指定本机 数据库用户名 数据库密码 数据库名 端口号 autocommit是是否自动提交
#     db = pymysql.connect(host='localhost', user='root', password='root', database='movie', port=3306, autocommit=False)
#     # 创建游标对象cursor
#     cursor = db.cursor()
#     # 使用execute()方法执行sql，如果表存在则删除
#     cursor.execute('drop table if EXISTS db_score_movie_count')
#     # 创建表的sql
#     sql = '''
#         create table db_score_movie_count(
#         `id` int(11) NOT NULL AUTO_INCREMENT,
#         `score` varchar(64) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
#         `count` int(11) NOT NULL,
#         PRIMARY KEY (`id`) USING BTREE
#         )
#     '''
#     cursor.execute(sql)
#     print('创建表成功')
# except:
#     print('创建表失败')
# finally:
#     # 关闭数据库连接
#     conn.close()


# 创建统计不同类型的电影数量最多的前十个类型的表
# try:
#     # 创建与数据库的连接
#     # 参数分别是 指定本机 数据库用户名 数据库密码 数据库名 端口号 autocommit是是否自动提交
#     db = pymysql.connect(host='localhost', user='root', password='root', database='movie', port=3306, autocommit=False)
#     # 创建游标对象cursor
#     cursor = db.cursor()
#     # 使用execute()方法执行sql，如果表存在则删除
#     cursor.execute('drop table if EXISTS db_type_movie_count')
#     # 创建表的sql
#     sql = '''
#         create table db_type_movie_count(
#         `id` int(11) NOT NULL AUTO_INCREMENT,
#         `type` varchar(64) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
#         `count` int(11) NOT NULL,
#         PRIMARY KEY (`id`) USING BTREE
#         )
#     '''
#     cursor.execute(sql)
#     print('创建表成功')
# except:
#     print('创建表失败')
# finally:
#     # 关闭数据库连接
#     conn.close()
