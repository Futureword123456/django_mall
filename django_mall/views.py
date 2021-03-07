# -*- coding: utf-8 -*-
# @Time : 2021/2/13 0013
# @Author : yang
# @Email : 2635681517@qq.com
# @File : views.py
import datetime

from django.shortcuts import render

# 定义index函数重定向到html文件
from system.models import Slider, News
from utils import constants


def index(request):
    # 查询首页轮播图
    slider_list = Slider.objects.filter(types=constants.SLIDER_TYPES_INDEX)
    # 首页的新闻
    now_time = datetime.datetime.now()

    news_list = News.objects.filter(types=constants.NEWS_TYPE_NEW, is_top=True, is_valid=True,
                                    start_time__lte=now_time,
                                    end_time__gte=now_time,
                                    )
    return render(request, 'index.html', {
        'slider_list': slider_list,
        'news_list': news_list
    })
