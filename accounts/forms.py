# -*- coding: utf-8 -*-
# @Time : 2021/3/26 0026
# @Author : yang
# @Email : 2635681517@qq.com
# @File : forms.py
import re

from django import forms
from django.contrib.auth import authenticate, login

from accounts.models import User
from utils.verify import VerifyCode


class UserLoginForm(forms.Form):
    """"用户登录创建表单"""
    """前台传到的后台数据"""
    username = forms.CharField(label='用户名', max_length=64)
    password = forms.CharField(label='密码', max_length=64, widget=forms.PasswordInput)
    verify_code = forms.CharField(label='验证码', max_length=5, error_messages={
        'required': '请输入验证码'
    })

    def __init__(self, request, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.request = request

    # def clean_username(self):
    #     """验证用户名,前端验证,每一个字段的验证"""
    #     """得到前端传的数据"""
    #     username = self.cleaned_data['username']
    #     print(username)
    #     # 判断用户名是否为手机号码
    #     pattern = r'^(13[0-9]|14[5|7]|15[0|1|2|3|4|5|6|7|8|9]|18[0|1|2|3|5|6|7|8|9])\d{8}$'
    #     if not username:
    #         raise forms.ValidationError('请输入用户名')
    #     if not re.search(pattern, username):
    #         raise forms.ValidationError('请输入正确的手机号码')
    #     return username

    def clean_password(self):
        """验证密码"""
        password = self.cleaned_data['password']
        print(password)
        if len(password) < 6 or len(password) > 12 or len(password) < 0:
            raise forms.ValidationError('请输入6到12位的密码')
        if not password:
            raise forms.ValidationError('请输入密码')
        return password

    def clean_verify_code(self):
        """ 验证用户输入的验证码是否正确 """
        verify_code = self.cleaned_data['verify_code']
        print(verify_code)
        if not verify_code:
            raise forms.ValidationError('请输入验证码')
        client = VerifyCode(self.request)
        if not client.validate_code(verify_code):
            raise forms.ValidationError('您输入的验证码不正确')
        return verify_code

    def clean(self):
        cleaned_data = super().clean()
        print(cleaned_data)
        # 获取用户名和密码 ，不建议使用[]的方式
        # username = cleaned_data['username']

        username = cleaned_data.get('username', None)
        password = cleaned_data.get('password', None)
        if username and password:
            # 查询用户名和密码匹配的用户
            user_list = User.objects.filter(username=username)
            if user_list.count() == 0:
                raise forms.ValidationError('用户名不存在')
            # # 验证密码是否正确
            # if not user_list.filter(password=password).exists():
            #     raise forms.ValidationError('密码错误')
            if not authenticate(username=username, password=password):
                raise forms.ValidationError('密码错误')
        return cleaned_data


class UserRegisterForm(forms.Form):
    """用户注册表单"""
    username = forms.CharField(label='用户名', max_length=64)
    password = forms.CharField(label='密码', max_length=64, widget=forms.PasswordInput)
    nickname = forms.CharField(label='昵称', max_length=64)
    repassword = forms.CharField(label='重复密码', max_length=64, widget=forms.PasswordInput)
    verify_code = forms.CharField(label='验证码', max_length=6)

    def __init__(self, request, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.request = request

    def clean_verify_code(self):
        """ 验证用户输入的验证码是否正确 """
        verify_code = self.cleaned_data['verify_code']
        print(verify_code)
        if not verify_code:
            raise forms.ValidationError('请输入验证码')
        client = VerifyCode(self.request)
        if not client.validate_code(verify_code):
            raise forms.ValidationError('您输入的验证码不正确')
        return verify_code

    def clean_username(self):
        """验证用户名是否已经被注册了"""
        data = self.cleaned_data['username']
        # 从数据库中查询
        if User.objects.filter(username=data).exists():
            raise forms.ValidationError('用户名已经存在')
        return data

    def clean_nickname(self):
        """验证昵称"""
        nickname = self.cleaned_data['nickname']
        if not nickname:
            raise forms.ValidationError('昵称不能为空')
        return nickname

    def clean_password(self):
        """验证密码"""
        password = self.cleaned_data['password']
        print(password)
        if len(password) < 6 or len(password) > 12 or len(password) < 0:
            raise forms.ValidationError('请输入6到12位的密码')
        if not password:
            raise forms.ValidationError('请输入密码')
        return password

    def clean(self):
        """验证密码和重复密码"""
        cleaned_data = super().clean()
        password = cleaned_data.get('password', None)
        repassword = cleaned_data.get('repassword', None)
        if password and repassword:
            if password != repassword:
                raise forms.ValidationError('两次密码不一样，请重新输入')
        return cleaned_data

    def register(self):
        """注册方法"""
        data = self.cleaned_data
        print(data)
        # 1、创建用户
        # User.objects.create_user(username=data['username'],
        #                          password=data['password'])
        User.objects.create_user(username=data['username'],
                                 password=data['password'],
                                 level=0,
                                 nickname=data['nickname'])

        # 2、自动登录
        user = authenticate(username=data['username'],
                            password=data['password'])
        login(self.request, user)
        return user
