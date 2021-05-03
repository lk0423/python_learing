# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, render_to_response
from django.http import HttpResponse
from django.template import RequestContext
from blogadmin import models
from django.core.paginator import Paginator, InvalidPage, EmptyPage, PageNotAnInteger
from django.db.models.query import QuerySet
from json import dumps
# from django.core.serializers.json import DjangojsonEncoder
from datetime import date, datetime
from django.http import jsonResponse


# 分页功能
def divide_page(request, articles):
    """
    :param request:  前端网页的url请求
    :param articles: 所有（分类）文章
    :return:   字典，分页后的文章列表和要显示的页码范围
    """
    if request.GET.get("page") == 'all':
        page = 1
        paginator = Paginator(object_list=articles, per_page=len(articles))
        articles_list = paginator.page(page)
        page_range = [1]
    else:
        before_range_num = 3  # 当前页前显示3页
        after_range_num = 2  # 当前页后显示2页，一共显示6个页码号
        list_per_page = 2  # 设置每页显示博文的数量
        try:
            # 如果请求的页码小于1或者类型错误，则默认第1页
            page = int(request.GET.get("page", 1))
            if page < 1:
                page = 1
        except ValueError:
            page = 1
        # 利用django自带分页Paginator
        # 常用属性:per_page: 每页显示条目数量;  count: 数据总个数;
        # num_pages:总页数;
        # page_range:总页数的索引范围，页码的范围，从1开始，例如[1, 2, 3, 4]。
        paginator = Paginator(object_list=articles, per_page=list_per_page)
        try:
            # 取得page页码处的Page对象
            articles_list = paginator.page(page)
        except(EmptyPage, InvalidPage, PageNotAnInteger):
            # 如果该页不存在或者超过则跳转到尾页
            articles_list = paginator.page(paginator.num_pages)
        # print("number of pages: %s " % paginator.num_pages)
        if paginator.num_pages >= after_range_num + before_range_num + 1:  # 总页数够摆满6个页码号
            if page >= paginator.num_pages - after_range_num:
                page_range = range(paginator.num_pages - before_range_num - after_range_num, paginator.num_pages + 1)
            elif page >= after_range_num + before_range_num:
                page_range = range(page - before_range_num, page + after_range_num + 1)
            else:
                page_range = range(1, 7)
        else:  # 总页数不够6个
            page_range = range(1, paginator.num_pages + 1)
            # 把博文列表和页码范围传参给前端模板
    return {'articles': articles_list, 'page_range': page_range}


# ------  首页Homepage  index.html  --------#
def index(request):
    # get four newest blog articles: title, category, abstract, update_time
    articles = models.Article.objects.all()
    # filmreviews = models.FilmReview.objects.all()

    # 用中文显示类别字段
    for i in articles:
        i.category = i.get_category_display()

    bloglist = {
        'blog1': articles[0],
        'blog2': articles[1],
        'blog3': articles[2],
        'blog4': articles[3],
        'blog5': articles[4],
    }
    # return render(request,'test.html',bloglist)
    return render(request, 'index.html', bloglist)


def tech(request):
    tech_articles = models.Article.objects.all()
    # return render(request,'tech.html', {'articles':tech_articles})
    # 先把所有数据都取出来分好页，然后根据请求的页码提取相应的数据段传给前端显示
    parameters_dict = divide_page(request, tech_articles)
    return render(request, 'tech.html', parameters_dict)


def chat(request):
    return HttpResponse("待开发")


def movie(request):
    # page = int(request.GET.get("page",0))  #如果请求的页码小于1或者类型错误，则默认第0页
    # newest_filmreviews = models.FilmReview.objects.all().order_by('-pub_time')[0:5]  # Queryset的切片取值，从发布时间最新的开始，每次显示5个博文
    newest_filmreviews = models.FilmReview.objects.order_by('-pub_time').values('id', 'title', 'pub_time')[0:5]
    return render(request, 'movie.html', {"newest_filmreviews": newest_filmreviews})


# def json_serial(obj):
#     """json serializer for objects not serializable by default json code"""
#     if isinstance(obj, (datetime, date)):
#         return obj.isoformat()
#     raise TypeError("Type %s not serializable" % type(obj))
# 
# 
# def queryset_to_json(querysetdata):
#     """json格式举例：
#     {"bloglist": [{'id':id,'title': "文章标题",'pub_time': "发布时间要转成正确格式"},
#             {"title": "文章标题","pub_time": "发布时间要转成正确格式"}]}
#     """
#     result = {'bloglist': []}
#     # #print('-------- 组装成json格式----------------->')
#     for i in querysetdata:
#         # print dumps(i.pub_time, default=json_serial)
#         result['bloglist'].append({'id': i.id, 'title': i.title,
#                                    'pub_time': dumps(i.pub_time, default=json_serial).strip(r'"').strip().split("T")[
#                                        0]})  # 时间要json序列化pub_time:""2017-08-28T17:15:27.550000+00:00""
#         # print('json格式数据： %s' % result)
#         # data_json = dumps(result, cls=DjangojsonEncoder)
#         # data_json = dumps(result)  #string
#         # return dumps(result)
#         print(result)
#     return jsonResponse(result)  # 返回json对象


def load_more(request):
    # data = models.FilmReview.objects.raw("SELECT id,title,pub_time FROM blogadmin_filmreview WHERE id=10;")[0]
    # print('----------MODELS取数据--------------->')
    # data = models.FilmReview.objects.all().values_list('id', 'title', 'pub_time')   # Queryset类型
    json_data = {}
    if request.method == 'POST' or request.method == 'GET':
        # print('请求是post类型')
        start = int(request.POST.get('offset', 0))
        size = int(request.POST.get('size', 0))
        # print("数据索引：%s %s" % (start,size))
        # 根据url的参数从数据库拉取相应的切片记录返回给ajax
        try:
            # data = models.FilmReview.objects.all()[start:(start + size)]
            data = models.FilmReview.objects.raw(
                'select id,title,strftime("%Y-%m-%d",pub_time)as p_time from blogadmin_filmreview  order by pub_time desc')[start:(start + size)]
            result = {'bloglist': []}
            if data:
                for i in data:
                    result['bloglist'].append({'id': i.id, 'title': i.title, 'pub_time': i.p_time})
                    json_data = jsonResponse(result)
                print(result)
                return json_data
            else:
                return jsonResponse(result)


        except Exception as err:
            print(err)

    else:  # 没有GET或POST请求
        print("没有请求，返回一个空json")
        return jsonResponse(json_data)


def book(request):
    return HttpResponse("待开发")


def tech_detail(request, id):
    # 根据前端请求的id获取单独的一篇文章
    try:
        article = models.Article.objects.get(id=str(id))
    except models.Article.DoesNotExist:
        raise Http404
    article.category = article.get_category_display()
    return render(request, 'techdetail.html', {'blog': article})


def movie_detail(request, id):
    # 根据前端请求的id获取单独的一篇影评
    try:
        article = models.FilmReview.objects.get(id=str(id))
    except models.FilmReview.DoesNotExist:
        raise Http404
    return render(request, 'moviedetail.html', {'blog': article})
