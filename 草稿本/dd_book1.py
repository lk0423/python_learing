# -*- coding: utf-8 -*-
from lxml import etree
from fake_useragent import UserAgent
import pymysql
import re, time
import requests

# 全局配置
headers = {
    "User-Agent": UserAgent().random
}


# 执行SQL指令
def save_db(password, database, sql_instruct):
    # 打开数据库连接
    db = pymysql.connect("localhost", "root", password, database)
    # 使用 cursor() 方法创建一个游标对象 cursor
    cursor = db.cursor()
    try:
        # 执行sql语句
        cursor.execute(sql_instruct)
        # 提交到数据库执行
        db.commit()
    except:
        # 如果发生错误则回滚
        db.rollback()
    # 关闭数据库连接
    db.close()


# 创建SQL指令
def build_sql(table, choice, result):
    sql = ''
    if choice == 1:
        sql = '''CREATE TABLE {} (
            id int(10) NOT NULL AUTO_INCREMENT,            
            title char(100) ,
            author char(200),
            price char(10),
            date char(20),
            comments char(10), 
             PRIMARY KEY ( `id` )
             )'''.format(table)  # 建库
    elif choice == 2:  # 插入
        sql = '''INSERT INTO {}(title ,author,price,date,comments) 
                VALUES ('{}','{}','{}','{}','{}') '''.format(table, result["title"], result["author"], result["price"],
                                                             result["date"],
                                                             result["comments"])
    return sql


# 一级页面爬取
def Page_Level(myPage):  # 一级页面
    dom = etree.HTML(myPage)
    results = []
    channels = dom.xpath('//*[@id="component_59"]/li')
    for channe in channels:
        result = {}
        result["title"] = channe.xpath('a/@title')[0]
        try:
            result["author"] = channe.xpath('p[@class="search_book_author"]/span[1]/a[1]/@title')[0]
        except:
            result["author"] = '未知'
        try:

            result["date"] = channe.xpath('p[@class="search_book_author"]/span[2]/text()')[0].replace('/', '')
        except:
            result["date"] = '未知'

        result["price"] = channe.xpath('p[@class="price"]/span[1]/text()')[0].replace('¥', '')
        comments = channe.xpath('p[@class="search_star_line"]/a/text()')[0]
        result["comments"] = re.findall('\d+', comments)[0]
        results.append(result)
    return results


# 爬虫
def spider(myPage):
    results = Page_Level(myPage)  # 爬取
    for result in results:
        sql_instruct2 = build_sql('dd_book', 2, result)
        save_db('5201314', 'data', sql_instruct2)  # 保存


# 运行
if __name__ == "__main__":
    sql_instruct1 = build_sql('dd_book', 1, '')
    save_db('5201314', 'data', sql_instruct1)
    base_url = 'http://search.dangdang.com/?key=%CA%E9%BC%AE&act=input&page_index='
    t = 1
    for i in range(1, t + 1):
        url = base_url + str(i)
        myPage = requests.get(url, headers=headers).text  # 获取源码
        time.sleep(2)
        spider(myPage)
