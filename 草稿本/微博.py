# -*- coding: utf-8 -*-
import requests                     # 困惑，每次拿到的网址不同，但内容却总是相同
from urllib.parse import urlencode
import json
import time
from lxml import etree

base_url = 'https://weibo.com/a/aj/transform/loadingmoreunlogin?'  # 基础url
headers = {
    'cookie': 'SUB=_2AkMq1ASHf8PxqwJRmPAcz2PlZIt3zQjEieKciPVcJRMxHRl-yT83qhcPtRB6AVQqaAA3PgnxzNjem2pQnC-aiL4Wr0FJ; SUBP=0033WrSXqPxfM72-Ws9jqgMF55529P9D9W53BS8s_e8vNhGbDdaoZCfX; SINAGLOBAL=7900137865049.919.1569229765919; UOR=,,localhost:63342; login_sid_t=fdd87361b2d82e49181abedfa87665ba; cross_origin_proto=SSL; Ugrow-G0=cf25a00b541269674d0feadd72dce35f; YF-V5-G0=4e19e5a0c5563f06026c6591dbc8029f; WBStorage=384d9091c43a87a5|undefined; _s_tentry=-; Apache=4950418691375.765.1569744259805; ULV=1569744259813:3:3:1:4950418691375.765.1569744259805:1569675320183; wb_view_log=1536*8641.25',
    'Host': 'weibo.com',  # 主机 端口号
    'Referer': 'https://weibo.com/',  # 页面跳转来源
    "User-Agent": 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.100 Safari/537.36',
    'X-Requested-With': 'XMLHttpRequest',  # 标记请求为 Ajax 请求
}


# 获取请求页面中的数据，json格式返回
def get_page(page):
    params = {  # 用于组合url的数据
        "ajwvr": "6",
        "category": "0",
        "page": page,
        "lefnav": "0",
        "cursor": "",
        "__rnd": str(int(time.time() * 1000))
    }
    url = base_url + urlencode(params)  # 组合url
    print(url)
    try:
        response = requests.get(url, headers=headers)  # 发起请求
        if response.status_code == 200:  # 若请求成功，则返回json格式的全部数据
            return response.json()
    except requests.ConnectionError as e:
        print('Error', e.args)


# 解析json数据，
def parse_page(json):
    if json:
        html_str = json.get('data')        # 这里得到是字符串
        html = etree.HTML(html_str)
        items = html.xpath("//div/ul/li")
        for item in items:
            item = item.xpath('div')
            for ite in item:
                weibo = {}
                text = ite.xpath('a/div/h3/text()') # 正文
                attitudes = ite.xpath('a/div/h4/span[1]/text()')  # 讨论数
                reading = ite.xpath('a/div/h4/span[2]/text()')  # 阅读数
                if text and attitudes and reading:
                    weibo['text'] = text[0]
                    weibo['attitudes'] = attitudes[0]
                    weibo['reading'] = reading[0]
                    yield weibo  # 构造一个生成器


# 保存数据
def save(result):
    with open('weibo.json', 'a') as f:
        f.write(json.dumps(result, ensure_ascii=False) + "\n")


if __name__ == '__main__':
    max_page = int(input("请输入要爬取的页面数："))
    for page in range(1, max_page + 1):
        json_data = get_page(page)  # 获取json格式的数据
        results = parse_page(json_data)  # 解析json数据，获得需要的结果
        for result in results:
            save(result)  # 保存为json文件
            print(result)
        time.sleep(3)
