# -*- coding: utf-8 -*-
# @Time : 2021/3/7 0007
# @Author : yang
# @Email : 2635681517@qq.com
# @File : urls.py
from django.urls import re_path
from tornado.web import url

from system import views
app_name = 'system'
urlpatterns = [
    # """新闻列表"""
    re_path(r'^news/$', views.news_list, name='news_list'),
    # 新闻详情
    re_path(r'^new/(?P<pk>\d+)/$', views.news_detail, name='news_detail'),
    # 验证码函数
    re_path(r'^verify/code/$', views.verify_code, name='verify_code'),

]
