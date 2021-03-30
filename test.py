# -*- coding: utf-8 -*-
# @Time : 2021/3/28 0028
# @Author : yang
# @Email : 2635681517@qq.com
# @File : test.py

# 通过contril创建一般用户
from django.contrib.auth.models import User
User.objects.create_user('yang','yang@qq.com','123456')
#创建超级管理员
# python manage.py createsuperuser
