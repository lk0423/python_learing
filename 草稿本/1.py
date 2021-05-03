import requests
from lxml import etree
from fake_useragent import UserAgent
import time

headers = {
    "User-Agent": UserAgent().random
}


# def Page_Level(myPage):
#     dom = etree.HTML(myPage)
#     zip_name_urls = []
#     channel = dom.xpath('/html/body/div[1]/div[2]/div/div/div/div/div/div/div[2]/p/span/span/span/text()')
#     for price in channel:
#         zip_name_urls.append(price)
#     return zip_name_urls
#
#
# def spider(url):
#     myPage = requests.get(url, headers=headers).content.decode("utf-8")  # 返回网页html源码
#     # print(myPage)
#     p = Page_Level(myPage)  # 爬取
#     sum = 0
#     for i in p:  # 计算价格
#         sum = sum + i
#     avg = sum / len(p)


if __name__ == "__main__":
    start = time.time()
    print('start......')
    for number in range(1, 6):
        start_url = "http://match.yuanrenxue.com/api/match/1?page=" + str(
            number) + "&m=2dc9eaf15404b26cd17e77e797de8f9c%E4%B8%A81602854059"
        # spider(start_url)
        print(start_url)
    print('end')
    end = time.time()
    print('爬虫运行时间为%.4f秒' % (end - start))
