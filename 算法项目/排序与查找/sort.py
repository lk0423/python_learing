from random import randint
import time

# def in_sort(list):                                                                               #1插入排序
#     t=len(list)
#     for i in range(1,t):
#         key=list[i]           #记录list[i]的值，使其不被遗漏
#         j=i-1                 #循环之用
#         while(j>=0):              #循环
#             if(key<list[j]):              #若key值（list[i]）更小
#                 list[j+1]=list[j]         #则将list[j]的值往后移
#                 list[j]=key               #将list[i]的值插入到原先list[j]的位置
#             else:
#                 break                 #否则，退出。因为前面的都已近排好序，没必要再往后继续
#             j-=1              #控制循环
#     return list
# **********************************************************************************************************************
#
# def bubble_sort(list):                                                                            #2冒泡排序
#     t = len(list)
#     for j in range(t):                #起泡
#         for i in range(1,t-j):        #使泡泡上升
#             if(list[i]<list[i-1]):    #比较，若后者小于前者
#                 list[i],list[i-1]=list[i-1],list[i]       #两个数交换（使用i-1是为了防止月越界）
#     return list
# #***********************************************************************************************************************
#
# def select_sort(list):                                                                            #3选择排序
#     t=len(list)
#     for i in range(t-1):      #外循环用于遍历整个列表
#         for j in range(i,t):  #内循环用于使一个数与整个列表的数比较
#             if list[i]>list[j]:
#                 list[i],list[j]=list[j],list[i]
#     return list
# #**********************************************************************************************************************
#
# def quick_sort(list):                                                                           #4快速排序
#     if list==[]:          #递归出口
#         return []
#     else:
#         list_first=list[0]        #每次都以第一个元素作为中间比较对象
#         list_less=quick_sort([m for m in list[1:] if m <= list_first])    #筛选比list[0]小的值，不断递归 直至递归出口
#         list_more=quick_sort([n for n in list[1:] if n >= list_first])
#         return list_less + [list_first] + list_more                   #始终让小的在一边，大的在另一边
# #**********************************************************************************************************************
#
# def merge_sort(list):                                                                              #5归并排序
#     if len(list)==1:
#         return list           #递归出口
#     mid=len(list)//2          #求中间值
#     left=list[:mid]                       #取前一半
#     right=list[mid:]                      #取后一半
#     ll=merge_sort(left)       #递归开始
#     rr=merge_sort(right)
#     return merge(ll,rr)       #调用下面的函数
#
# def merge(ll,rr):             #（粗）排序（多次进行）
#     result=[]
#     while len(ll)>0 and len(rr)>0:    #两个列表均不为空时进行，筛选出两边相比而言小的，一步一步放进result中
#         if ll[0]<=rr[0]:
#             result.append(ll.pop(0))
#         else:
#             result.append(rr.pop(0))
#     result +=ll       #若有一方未筛选完，则可通过此步放入其中
#     result +=rr
#     return result
# #**********************************************************************************************************************
#
# def shell_sort(list):                                                                               #6希尔排序
#     t=len(list)
#     dist=t//2         #取中间值
#     while dist>0:     # 判断list中元素不止一个
#         for i in range(dist,t):       #dist 控制大循环，并且每次取后一半循环
#             temp=list[i]              #中间变量存储后一半中所有的值
#             j=i
#             while j>=dist and temp<list[j-dist]:      # j-dist 是相对 dist 处的前一半的与 j 相同位置的元素
#                 list[j]=list[j-dist]          #若 temp 比前一半处的数小，则使temp处为前面的那个小的值
#                 j-=dist                       #若循环得以执行，则不断回到 前一半处
#                 list[j]=temp                  #将后面那个大的值temp 放到前面那个位置上
#         dist//=2      #将for循环步步推进，dist不断减小，后一半中实际的值增多，最终使dist小于零（list已不能再分），退出while
#     return list
# #**********************************************************************************************************************


# ************************************************测试主函数**************************************************************
def main():
    lk = []
    for i in range(10):
        k = randint(1,1000)
        lk.append(k)
    time0=time.time()
    # print(      bubble_sort      (lk))
    p=sorted(lk)
    # p.reverse()
    print(p)
    time1=time.time()
    print(time1-time0)

if __name__ == '__main__':
    main()
