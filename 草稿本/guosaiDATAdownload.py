# -*- coding: utf-8 -*-
from lxml import etree
import os, time
import pymysql
import urllib.request


def write_to_file(save_path, filename, results):  # 保存为CSV文件
    if not os.path.exists(save_path):  # 判断文件路径是否存在，若不在，则创建
        os.mkdir(save_path)
    path = save_path + "/" + filename + ".txt"
    with open(path, 'a+', encoding='utf-8') as fp:
        for i in results:
            fp.write("%s\n" % (i))


def write_to_mysql(sp_id, rare, url, tags):
    db = pymysql.connect("localhost", "root", "5201314", "subway")
    cursor = db.cursor()
    sql = "INSERT INTO smallphoto(sp_id, rare, url, tags) VALUES ('{}', '{}', '{}', '{}') ".format(sp_id, rare, url,
                                                                                                   tags)
    try:
        cursor.execute(sql)
        db.commit()
    except:
        db.rollback()
    db.close()


if __name__ == "__main__":
    j = 90001
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
        a_url = base_url + zhongjianurl
        request1 = urllib.request.Request(a_url)
        response1 = urllib.request.urlopen(request1)
        html1 = response1.read().decode('utf-8')
        dom1 = etree.HTML(html1)
        channel_names1 = dom1.xpath('/html/body/pre/a/@href')
        i = -1
        rares = ['A', 'B', 'C', 'D']
        time.sleep(1)
        for lasturl in channel_names1:
            time.sleep(0.5)
            if i == -1:
                i = 0
                continue
            lk = a_url + lasturl
            sp_id = 'sp' + str(j)
            rare = rares[i]
            url = lk
            tags = i + 1 + 10
            write_to_mysql(sp_id, rare, url, tags)  # 存入数据库
            # lk = 'sp' + str(j) + '  ' + rares[i] + '  ' + lk + '  ' + str(i)
            print(i)
            # list.append(lk)
            i += 1
            j += 1
    # write_to_file('D:\桌面', 'lk123456', list)
