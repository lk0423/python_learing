# -*- coding: utf-8 -*-
from selenium import webdriver          # 失败
from lxml import etree
from selenium.webdriver.common.keys import Keys

import time


driver = webdriver.Firefox()
driver.get("https://wenku.baidu.com/view/2f3f831368eae009581b6bd97f1922791688bed6.html?from=search")
driver.find_element_by_xpath('//*[@id="html-reader-go-more"]/div[2]/div[1]/span/span[2]').click()
# time.sleep(60)
for i in range(60):
    driver.find_element_by_id("pageNo-1").send_keys(Keys.ARROW_DOWN)
time.sleep(3)
driver.save_screenshot("lk.png")
p = driver.page_source

# words = etree.HTML(p).xpath('//*[@id="reader-container-inner-1"]/div')
path = 'lk.txt'               # 路径
# n = len(words)
# num = range(1,n+1)
# for word,i in zip(words,num):
#     try:
#         txt = etree.HTML(word).xpath('*[@id="pageNo-' + str(i) + '"]/div/div/div/div[2]/div/p/text()')
#         print(txt)
#     except:
#         print("error")


for i in range(50):
    try:
        txt = etree.HTML(p).xpath('//*[@id="pageNo-' + str(i) + '"]/div/div/div/div[2]/div/p/text()')
        print(txt)
    # except:
    #     print("error")
    #
    # # 保存文件
    # try:
        f = open(path, 'a+', encoding='utf-8')              # 打开
        for t in txt:
            f.write("%s\n" % (t))                   # 写入内容
        f.close()                               # 关闭
    except:
        print("error")
