# -*- coding: utf-8 -*-
from lxml import etree
import time
import pymysql
import re
url = 'http://push2.eastmoney.com/api/qt/clist/get?pn=1&pz=100&po=1&np=1&ut=b2884a393a59ad64002292a3e90d46a5&fltt=2&invt=2&fid=f184&fid0=f4001&fields=f2,f3,f12,f13,f14,f62,f184,f225,f165,f263,f109,f175,f264,f160,f100,f124,f265&fs=m:0+t:6+f:!2,m:0+t:13+f:!2,m:0+t:80+f:!2,m:1+t:2+f:!2,m:1+t:23+f:!2&rt=53171656&cb=jQuery1830902701342662777_1595149682438&_=1595149689946'


def create_db(the_stock_name):
    # 打开数据库连接
    db = pymysql.connect("10.21.30.15", "root", "123456", "data")
    # 使用 cursor() 方法创建一个游标对象 cursor
    cursor = db.cursor()
    cursor.execute("DROP TABLE IF EXISTS {}".format(the_stock_name))
    # 使用预处理语句创建表
    sql = "CREATE TABLE {} ( \
             w_id int(20) NOT NULL AUTO_INCREMENT,\
             stock_code varchar(20),\
             stock_name varchar(20),\
             stock_data_src varchar(255),\
             stock_new_price varchar(20),\
             stock_new_rank varchar(20),\
             stock_new_float varchar(20),\
             stock_module varchar(20),\
             PRIMARY KEY ( `w_id` )\
             )".format(the_stock_name)
    try:
        # 执行sql语句
        cursor.execute(sql)
        # 提交到数据库执行
        db.commit()
    except:
        # 如果发生错误则回滚
        db.rollback()
    # 关闭数据库连接
    db.close()


def save_db(the_stock_name, items):
    # 打开数据库连接
    db = pymysql.connect("localhost", "root", "123456", "data")
    # 使用 cursor() 方法创建一个游标对象 cursor
    cursor = db.cursor()
    for item in items:
        stock_code = item['股票代码']
        stock_name = item['股票名称']
        stock_data_src = item['数据地址']
        stock_new_price = item['今日价格']
        stock_new_rank = item['今日排名']
        stock_new_float = item['今日涨跌']
        stock_module = item['所属模块']

        sql = "INSERT INTO {}(stock_code,stock_name,stock_data_src,stock_new_price,stock_new_rank,stock_new_float,stock_module) VALUES ('{}', '{}','{}', '{}', '{}', '{}','{}') ".format(
            the_stock_name, stock_code, stock_name, stock_data_src, stock_new_price, stock_new_rank, stock_new_float,
            stock_module)
        try:
            # 执行sql语句
            cursor.execute(sql)
            # 提交到数据库执行
            db.commit()
        except:
            # 如果发生错误则回滚
            db.rollback()
    # 关闭数据库连接
    db.close()



