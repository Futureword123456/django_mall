from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes.fields import GenericForeignKey
from django.db import models

from utils import constants


class Slider(models.Model):
    """ 系统轮播图 """
    name = models.CharField('名称', max_length=32)
    desc = models.CharField('描述', max_length=100, null=True, blank=True)
    types = models.SmallIntegerField('展现位置',
                                     choices=constants.SLIDER_TYPES_CHOICES,
                                     default=constants.SLIDER_TYPES_INDEX)
    img = models.ImageField('图片', upload_to='slider')
    reorder = models.SmallIntegerField('排序', default=0, help_text='数字越大，越靠前')
    start_time = models.DateTimeField('生效开始时间', null=True, blank=True)
    end_time = models.DateTimeField('生效结束时间', null=True, blank=True)

    target_url = models.CharField('跳转地址', max_length=255, null=True, blank=True)
    is_valid = models.BooleanField('是否删除', default=True)

    created_at = models.DateTimeField('创建时间', auto_now_add=True)
    updated_at = models.DateTimeField('最后修改时间', auto_now=True)

    class Meta:
        db_table = 'system_slider'
        ordering = ['-reorder']


class News(models.Model):
    """ 新闻及通知 """
    types = models.SmallIntegerField('类型', choices=constants.NEWS_TYPES_CHOICE,
                                     default=constants.NEWS_TYPE_NEW)
    title = models.CharField('标题', max_length=255)
    content = models.TextField('内容')
    reorder = models.SmallIntegerField('排序', default=0, help_text='数字越大，越靠前')
    start_time = models.DateTimeField('生效开始时间', null=True, blank=True)
    end_time = models.DateTimeField('生效结束时间', null=True, blank=True)
    view_count = models.IntegerField('浏览次数', default=0)

    is_top = models.BooleanField('是否置顶', default=False)
    is_valid = models.BooleanField('是否删除', default=True)

    created_at = models.DateTimeField('创建时间', auto_now_add=True)
    updated_at = models.DateTimeField('最后修改时间', auto_now=True)

    class Meta:
        db_table = 'system_news'
        ordering = ['-reorder']


class ImageFile(models.Model):
    """ 图片表 """
    # 201902/xxxx
    img = models.ImageField('图片', upload_to='%Y%m/images/')
    summary = models.CharField('图片名称', max_length=200)

    # 复合关联
    content_type = models.ForeignKey(ContentType,on_delete=models.CASCADE)
    object_id = models.PositiveIntegerField()
    content_object = GenericForeignKey('content_type', 'object_id')

    is_valid = models.BooleanField('是否有效', default=True)

    created_at = models.DateTimeField('创建时间', auto_now_add=True)
    updated_at = models.DateTimeField('修改时间', auto_now=True)

    class Meta:
        db_table = 'system_images'
