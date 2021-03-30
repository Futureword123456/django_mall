"""django_mall URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from django.urls import path, include

from django_mall import views

urlpatterns = [
    path('admin/', admin.site.urls),
    # 配置根目录
    url(r'^$', views.index, name='index'),
    # 商品详情
    url(r'^mall/',include('mall.urls',namespace='mall')),
    # 系统模块
    url(r'^accounts/',include('accounts.urls',namespace='accounts')),
    # 系统模块
    url(r'^system/',include('system.urls',namespace='system')),


]



