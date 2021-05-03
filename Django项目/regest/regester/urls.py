from django.urls import path
from . import views

# APP中的路由（本地路由）
urlpatterns = [
    path('', views.index),                  # 网站首页
    path('baidu/', views.generate_qrcode),  # 自动生成百度二维码的网页地址
    path('login/', views.login),            # 登录注册的网页地址
]
