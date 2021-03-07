# -*- coding: utf-8 -*-
# @Time : 2021/2/15 0015
# @Author : yang
# @Email : 2635681517@qq.com
# @File : urls.py
from django.conf.urls import url

from mall import views
app_name = 'mall'
urlpatterns = [
    # 商品列表
    url(r'^prod/list$', views.product_list, name='product_list'),
    # 商品详情
    url(r'^prod/detail/(?P<pk>\S+)/$', views.product_detail, name='product_detail'),
]
