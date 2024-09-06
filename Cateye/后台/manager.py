import json

from flask import Flask, request, jsonify, Response
import pymysql
from flask.json import JSONEncoder
from flask_cors import *

app = Flask(__name__)
app.config['JSON_AS_ASCII'] = False
CORS(app, supports_credentials=True)

# app.json = json.JSONDecoder


# app.json_encoder = JSONEncoder

@app.route('/page1', methods=['GET'])
def page1():
    data_type = request.args.get('movie_type',type=str)
    if data_type is None:
        return jsonify(code=400,message='movie_type参数不能为空')
    sql = "SELECT SUM(movie_booking) from db_movie where `movie_publish_year` = 1954 and `movie_type` LIKE '%" + str(data_type) + "%' " \
     " UNION SELECT SUM(movie_booking) from db_movie where `movie_publish_year` = 1979 and `movie_type` LIKE '%" + str(data_type) + "%' " \
     " UNION SELECT SUM(movie_booking) from db_movie where `movie_publish_year` = 1984 and `movie_type` LIKE '%" + str(data_type) + "%' " \
     " UNION SELECT SUM(movie_booking) from db_movie where `movie_publish_year` = 1988 and `movie_type` LIKE '%" + str(data_type) + "%' " \
     " UNION SELECT SUM(movie_booking) from db_movie where `movie_publish_year` = 1989 and `movie_type` LIKE '%" + str(data_type) + "%' " \
     " UNION SELECT SUM(movie_booking) from db_movie where `movie_publish_year` = 1991 and `movie_type` LIKE '%" + str(data_type) + "%' " \
     " UNION SELECT SUM(movie_booking) from db_movie where `movie_publish_year` = 1992 and `movie_type` LIKE '%" + str(data_type) + "%' " \
     " UNION SELECT SUM(movie_booking) from db_movie where `movie_publish_year` = 1993 and `movie_type` LIKE '%" + str(data_type) + "%' " \
     " UNION SELECT SUM(movie_booking) from db_movie where `movie_publish_year` = 1995 and `movie_type` LIKE '%" + str(data_type) + "%' " \
     " UNION SELECT SUM(movie_booking) from db_movie where `movie_publish_year` = 1997 and `movie_type` LIKE '%" + str(data_type) + "%' " \
     " UNION SELECT SUM(movie_booking) from db_movie where `movie_publish_year` = 1998 and `movie_type` LIKE '%" + str(data_type) + "%' " \
     " UNION SELECT SUM(movie_booking) from db_movie where `movie_publish_year` = 1999 and `movie_type` LIKE '%" + str(data_type) + "%' " \
     " UNION SELECT SUM(movie_booking) from db_movie where `movie_publish_year` = 2001 and `movie_type` LIKE '%" + str(data_type) + "%' " \
     " UNION SELECT SUM(movie_booking) from db_movie where `movie_publish_year` = 2002 and `movie_type` LIKE '%" + str(data_type) + "%' " \
     " UNION SELECT SUM(movie_booking) from db_movie where `movie_publish_year` = 2003 and `movie_type` LIKE '%" + str(data_type) + "%' " \
     " UNION SELECT SUM(movie_booking) from db_movie where `movie_publish_year` = 2004 and `movie_type` LIKE '%" + str(data_type) + "%' " \
     " UNION SELECT SUM(movie_booking) from db_movie where `movie_publish_year` = 2005 and `movie_type` LIKE '%" + str(data_type) + "%' " \
     " UNION SELECT SUM(movie_booking) from db_movie where `movie_publish_year` = 2006 and `movie_type` LIKE '%" + str(data_type) + "%' " \
     " UNION SELECT SUM(movie_booking) from db_movie where `movie_publish_year` = 2007 and `movie_type` LIKE '%" + str(data_type) + "%' " \
     " UNION SELECT SUM(movie_booking) from db_movie where `movie_publish_year` = 2008 and `movie_type` LIKE '%" + str(data_type) + "%' " \
     " UNION SELECT SUM(movie_booking) from db_movie where `movie_publish_year` = 2009 and `movie_type` LIKE '%" + str(data_type) + "%' " \
     " UNION SELECT SUM(movie_booking) from db_movie where `movie_publish_year` = 2010 and `movie_type` LIKE '%" + str(data_type) + "%' " \
     " UNION SELECT SUM(movie_booking) from db_movie where `movie_publish_year` = 2011 and `movie_type` LIKE '%" + str(data_type) + "%' " \
     " UNION SELECT SUM(movie_booking) from db_movie where `movie_publish_year` = 2012 and `movie_type` LIKE '%" + str(data_type) + "%' " \
     " UNION SELECT SUM(movie_booking) from db_movie where `movie_publish_year` = 2013 and `movie_type` LIKE '%" + str(data_type) + "%' " \
     " UNION SELECT SUM(movie_booking) from db_movie where `movie_publish_year` = 2014 and `movie_type` LIKE '%" + str(data_type) + "%' " \
     " UNION SELECT SUM(movie_booking) from db_movie where `movie_publish_year` = 2015 and `movie_type` LIKE '%" + str(data_type) + "%' " \
     " UNION SELECT SUM(movie_booking) from db_movie where `movie_publish_year` = 2016 and `movie_type` LIKE '%" + str(data_type) + "%' " \
     " UNION SELECT SUM(movie_booking) from db_movie where `movie_publish_year` = 2017 and `movie_type` LIKE '%" + str(data_type) + "%' " \
     " UNION SELECT SUM(movie_booking) from db_movie where `movie_publish_year` = 2018 and `movie_type` LIKE '%" + str(data_type) + "%' " \
     " UNION SELECT SUM(movie_booking) from db_movie where `movie_publish_year` = 2019 and `movie_type` LIKE '%" + str(data_type) + "%' " \
     " UNION SELECT SUM(movie_booking) from db_movie where `movie_publish_year` = 2020 and `movie_type` LIKE '%" + str(data_type) + "%' " \
     " UNION SELECT SUM(movie_booking) from db_movie where `movie_publish_year` = 2021 and `movie_type` LIKE '%" + str(data_type) + "%' " \
     " UNION SELECT SUM(movie_booking) from db_movie where `movie_publish_year` = 2022 and `movie_type` LIKE '%" + str(data_type) + "%' " \
     " UNION SELECT SUM(movie_booking) from db_movie where `movie_publish_year` = 2023 and `movie_type` LIKE '%" + str(data_type) + "%' " \
     " UNION SELECT SUM(movie_booking) from db_movie where `movie_publish_year` = 2024 and `movie_type` LIKE '%" + str(data_type) + "%' "
    conn = pymysql.connect(host='localhost', user='root', password='root', port=3306, db='movie',
                           charset='utf8mb4')
    cursor = conn.cursor()
    cursor.execute(sql)
    values = cursor.fetchall()
    cursor = conn.cursor(cursor=pymysql.cursors.DictCursor)
    jsondata = {}
    xd = []
    for index, i in enumerate(values):
        xd.append(i[0])
    jsondata['data'] = xd
    cursor.close()
    conn.close()
    return jsonify(jsondata)

@app.route('/page2', methods=['GET'])
def page2():
    import werkzeug
    try:
        data_year = int(request.args['year'])
        data_top = int(request.args['top'])
    except werkzeug.exceptions.BadRequestKeyError:
        return jsonify(code=400, message='缺少year或top参数')
    sql = "SELECT `movie_name`,movie_booking from db_movie WHERE `movie_publish_year` = " + str(data_year) + \
          " ORDER BY movie_booking DESC LIMIT 0," + str(data_top)
    conn = pymysql.connect(host='localhost', user='root', password='root', port=3306, db='movie',
                           charset='utf8mb4')
    cursor = conn.cursor()
    cursor.execute(sql)
    values = cursor.fetchall()
    cursor = conn.cursor(cursor=pymysql.cursors.DictCursor)
    jsondata = {}
    datas = []
    for index, i in enumerate(values):
        mydict = {}
        mydict["value"] = i[1]
        mydict["name"] = i[0]
        datas.append(mydict)
    jsondata['datas'] = datas
    cursor.close()
    conn.close()
    return jsonify(jsondata)


@app.route('/page3', methods=['GET'])
def page3():
    import werkzeug
    try:
        data_year = int(request.args['year'])
        data_month = int(request.args['month'])
    except werkzeug.exceptions.BadRequestKeyError:
        return jsonify(code=400, message='缺少year或month参数')
    sql = " SELECT SUM(movie_booking) from db_movie where movie_type LIKE '%喜剧%' and `movie_publish_year` = " + str(
        data_year) + " and `movie_publish_month` = " + str(data_month) + \
          " UNION SELECT SUM(movie_booking) from db_movie where movie_type LIKE '%冒险%' and `movie_publish_year` = " + str(
        data_year) + " and `movie_publish_month` = " + str(data_month) + \
          " UNION SELECT SUM(movie_booking) from db_movie where movie_type LIKE '%传记%' and `movie_publish_year` = " + str(
        data_year) + " and `movie_publish_month` = " + str(data_month) + \
          " UNION SELECT SUM(movie_booking) from db_movie where movie_type LIKE '%剧情%' and `movie_publish_year` = " + str(
        data_year) + " and `movie_publish_month` = " + str(data_month) + \
          " UNION SELECT SUM(movie_booking) from db_movie where movie_type LIKE '%战争%' and `movie_publish_year` = " + str(
        data_year) + " and `movie_publish_month` = " + str(data_month) + \
          " UNION SELECT SUM(movie_booking) from db_movie where movie_type LIKE '%奇幻%' and `movie_publish_year` = " + str(
        data_year) + " and `movie_publish_month` = " + str(data_month) + \
          " UNION SELECT SUM(movie_booking) from db_movie where movie_type LIKE '%家庭%' and `movie_publish_year` = " + str(
        data_year) + " and `movie_publish_month` = " + str(data_month) + \
          " UNION SELECT SUM(movie_booking) from db_movie where movie_type LIKE '%历史%' and `movie_publish_year` = " + str(
        data_year) + " and `movie_publish_month` = " + str(data_month) + \
          " UNION SELECT SUM(movie_booking) from db_movie where movie_type LIKE '%科幻%' and `movie_publish_year` = " + str(
        data_year) + " and `movie_publish_month` = " + str(data_month) + \
          " UNION SELECT SUM(movie_booking) from db_movie where movie_type LIKE '%惊悚%' and `movie_publish_year` = " + str(
        data_year) + " and `movie_publish_month` = " + str(data_month) + \
          " UNION SELECT SUM(movie_booking) from db_movie where movie_type LIKE '%悬疑%' and `movie_publish_year` = " + str(
        data_year) + " and `movie_publish_month` = " + str(data_month) + \
          " UNION SELECT SUM(movie_booking) from db_movie where movie_type LIKE '%爱情%' and `movie_publish_year` = " + str(
        data_year) + " and `movie_publish_month` = " + str(data_month) + \
          " UNION SELECT SUM(movie_booking) from db_movie where movie_type LIKE '%犯罪%' and `movie_publish_year` = " + str(
        data_year) + " and `movie_publish_month` = " + str(data_month) + \
          " UNION SELECT SUM(movie_booking) from db_movie where movie_type LIKE '%动画%' and `movie_publish_year` = " + str(
        data_year) + " and `movie_publish_month` = " + str(data_month) + \
          " UNION SELECT SUM(movie_booking) from db_movie where movie_type LIKE '%运动%' and `movie_publish_year` = " + str(
        data_year) + " and `movie_publish_month` = " + str(data_month) + \
          " UNION SELECT SUM(movie_booking) from db_movie where movie_type LIKE '%恐怖%' and `movie_publish_year` = " + str(
        data_year) + " and `movie_publish_month` = " + str(data_month) + \
          " UNION SELECT SUM(movie_booking) from db_movie where movie_type LIKE '%纪录片%' and `movie_publish_year` = " + str(
        data_year) + " and `movie_publish_month` = " + str(data_month) + \
          " UNION SELECT SUM(movie_booking) from db_movie where movie_type LIKE '%动作%' and `movie_publish_year` = " + str(
        data_year) + " and `movie_publish_month` = " + str(data_month)
    conn = pymysql.connect(host='localhost', user='root', password='root', port=3306, db='movie',
                           charset='utf8mb4')
    cursor = conn.cursor()
    cursor.execute(sql)
    values = cursor.fetchall()
    cursor = conn.cursor(cursor=pymysql.cursors.DictCursor)
    jsondata = {}
    xd = []
    yd = ['喜剧', '冒险', '传记', '剧情', '战争', '奇幻', '家庭', '历史', '科幻',
          '惊悚', '悬疑', '爱情', '犯罪', '动画', '运动', '恐怖', '纪录片', '动作']
    datas = []
    for index, i in enumerate(values):
        mydict = {}
        mydict["value"] = i[0]
        mydict["name"] = yd[index]
        datas.append(mydict)
        xd.append(i[0])
    jsondata['category'] = yd
    jsondata['data'] = xd
    jsondata['datas'] = datas
    cursor.close()
    conn.close()
    return Response(json.dumps(jsondata), mimetype='application/json')


@app.route('/data', methods=['GET'])
def data():
    limit = int(request.args['limit'])
    page = int(request.args['page'])
    page = (page - 1) * limit
    conn = pymysql.connect(host='localhost', user='root', password='root', port=3306, db='movie',
                           charset='utf8mb4')

    cursor = conn.cursor()
    cursor.execute("select count(*) from db_movie")
    count = cursor.fetchall()
    cursor = conn.cursor(cursor=pymysql.cursors.DictCursor)
    cursor.execute("select * from db_movie limit " + str(page) + "," + str(limit))
    data_dict = []
    result = cursor.fetchall()
    for field in result:
        data_dict.append(field)
    table_result = {"code": 0, "msg": None, "count": count[0], "data": data_dict}
    cursor.close()
    conn.close()
    return jsonify(table_result)


@app.route('/addUser', methods=['POST'])
def addUser():
    get_json = request.get_json()
    name = get_json['name']
    password = get_json['password']
    conn = pymysql.connect(host='localhost', user='root', password='root', port=3306, db='movie',
                           charset='utf8mb4')
    cursor = conn.cursor()
    sql = "insert into `userinfo` values('" + name + "','" + password + "')"
    cursor.execute(sql)
    conn.commit()
    table_result = {"code": 200, "msg": "成功"}
    cursor.close()
    conn.close()
    return jsonify(table_result)


@app.route('/loginByPassword', methods=['POST'])
def loginByPassword():
    get_json = request.get_json()
    name = get_json['name']
    password = get_json['password']
    conn = pymysql.connect(host='localhost', user='root', password='root', port=3306, db='movie',
                           charset='utf8mb4')
    cursor = conn.cursor()
    cursor.execute("select count(*) from `userinfo` where `name` = '" + name + "' and password = '" + password + "'");
    count = cursor.fetchall()
    if count[0][0] != 0:
        table_result = {"code": 200, "msg": "成功"}
    else:
        table_result = {"code": 500, "msg": "失败"}
    cursor.close()
    conn.close()
    return jsonify(table_result)


if __name__ == "__main__":
    app.run(port=5000,debug=True)
