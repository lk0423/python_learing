from django.urls import path
from . import views

# APP�е�·�ɣ�����·�ɣ�
urlpatterns = [
    path('', views.index),                  # ��վ��ҳ
    path('baidu/', views.generate_qrcode),  # �Զ����ɰٶȶ�ά�����ҳ��ַ
    path('login/', views.login),            # ��¼ע�����ҳ��ַ
]
