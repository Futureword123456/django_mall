# -*- coding: utf-8 -*-
# @Time : 2021/3/26 0026
# @Author : yang
# @Email : 2635681517@qq.com
# @File : urls.py
from django.conf.urls import url

from accounts import views

app_name = 'account'
urlpatterns = [
    # 用户登录
    url(r'^user/login$', views.user_login, name='user_login'),
    # 用户退出
    url(r'^user/logout$', views.user_logout, name='user_logout'),
    # 用户注册
    url(r'^user/register$', views.user_register, name='user_register'),

]

