# -*- coding: utf-8 -*-
import pymysql
import urllib.request
from lxml import etree


def write_to_user_active_sites():  # 写入user_active_sites表数据
    db = pymysql.connect("localhost", "root", "5201314", "mysubway")
    cursor = db.cursor()
    try:
        u_id = 'u10002'
        for i in range(10001, 10046):
            p_id = 'p' + str(i)
            sql = "INSERT INTO user_active_sites(u_id, p_id, active) VALUES ('{}', '{}' , 0 ) ".format(u_id,
                                                                                                   p_id)
            cursor.execute(sql)
        db.commit()
    except:
        db.rollback()
    db.close()


def write_to_photo():  # 写入photo表数据
    db = pymysql.connect("localhost", "root", "5201314", "mysubway")
    cursor = db.cursor()
    try:
        j = 10001
        k = 0
        for i in range(90001, 90181):
            if k == 4:
                k = 0
                j += 1
            p_id = 'p' + str(j)
            sp_id = 'sp' + str(i)
            k += 1
            sql = "INSERT INTO photo(p_id, sp_id) VALUES ('{}', '{}') ".format(p_id, sp_id)
            cursor.execute(sql)
        db.commit()
    except:
        db.rollback()
    db.close()


def write_to_mysql_sites(list):
    db = pymysql.connect("localhost", "root", "5201314", "mysubway")
    cursor = db.cursor()
    try:
        i = 10001
        for s_name in list:
            s_id = 's' + str(i)
            p_id = 'p' + str(i)
            sql = "INSERT INTO sites(s_id,s_name, p_id) VALUES ('{}', '{}','{}') ".format(s_id, s_name, p_id)
            cursor.execute(sql)
            i += 1
            if i == 10046:
                break
        db.commit()
    except:
        db.rollback()
    db.close()


def write_to_sites():  # 写入sites表数据
    list = []
    base_url = "http://114.116.224.187:8081/grayPuzzle/"
    request = urllib.request.Request(base_url)
    response = urllib.request.urlopen(request)
    html = response.read().decode('utf-8')
    dom = etree.HTML(html)
    channel_names = dom.xpath('/html/body/pre/a/@href')
    lk123 = 0
    for zhongjianurl in channel_names:
        if lk123 == 0:
            lk123 = 100
            continue
        zs = zhongjianurl.replace(r'/', '')
        list.append(zs)
    print(list)
    write_to_mysql_sites(list)


if __name__ == "__main__":
    # write_to_photo()  # 写入photo表数据
    # write_to_sites()  # 写入sites表数据
    write_to_user_active_sites()  # 写入user_active_sites表数据
