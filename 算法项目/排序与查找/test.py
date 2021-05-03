import random
import time

n = int(input("输入机选的注数："))
start = time.time()
red_balls = []
for i in range(n):
    while len(red_balls) <= 6:
        a = random.randint(1, 33)
        if a not in red_balls:
            red_balls.append(a)
    red_balls.sort()
    print("红球：", end=" ")
    for i in range(len(red_balls)):
        if red_balls[i] < 10:
            print("0" + str(red_balls[i]), end=" ")
        else:
            print(str(red_balls[i]), end=" ")
    blue = random.randint(1, 16)
    if blue < 10:
        print("篮球：" + "0" + str(blue))
    else:
        print("篮球：" + str(blue))
    red_balls.clear()

end = time.time()
print("程序执行时间为：%.4f秒" % (end - start))

# def load_dic(filename):
#     f=open(filename)
#     word_dic=set()
#     max_length=1 #记录中文词的最大长度
#     for line in f:#取出每个中文单词，统一用unicode编码，这样每
# #个中文单词都用固定长度4个字节存储
#         word=unicode(line.strip(),'utf-8')
#         word_dic.add(word)
#         if len(word)>max_length:
#             max_length=len(word)
#     return max_length,word_d
#
# #正向最大匹配分词
# def fm_word_seg(sentence,max_length,word_dict):
#     begin=0
#     words=[]
#     sentence=unicode(sentence,'gb2312')
#     while begin<len(sentence):
#         for end in range(begin+max_length,begin,-1):
#             if sentence[begin:end] in word_dict:
#                 words.append(sentence[begin:end])
#                 break
#         begin=end
#     return words
#
# max_len,word_dict=load_dict(‘l.txt’)
# sent=raw_input(‘请输入一句中文：’)
# words=fmm_word_seg(sent,max_len,word_dict)
# for word in words:
#     print(word)
