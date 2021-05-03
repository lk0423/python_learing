from django.urls import path
from . import views
urlpatterns = [
    path('msggate/', views.msgproc),
    path('', views.hello),

]