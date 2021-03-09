import uuid

from django.db import models

# Create your models here.
from utils import constants


class Classify(models.Model):
    """商品的分类"""
    uid = models.UUIDField('分类ID', default=uuid.uuid4, editable=True)
    """自己关联自己一个分类下还有分类"""
    parent = models.ForeignKey('self', related_name='children')
    img = models.ImageField('分类图片', upload_to='classify')
    code = models.CharField('编码', max_length=32, null=True, blank=True)
    name = models.CharField('名称', max_length=12)
    desc = models.CharField('描述', max_length=64, null=True, blank=True)
    reorder = models.SmallIntegerField('排序', default=0)
    is_valid = models.BooleanField('是否有效', default=True)
    created_at = models.DateTimeField('创建时间', auto_now_add=True)
    updated_at = models.DateTimeField('修改时间', auto_now=True)

    class Meta:
        db_table = 'mall_classify'


class Tag(models.Model):
    """商品的标签"""
    uid = models.UUIDField("标签ID",default=uuid.uuid4,editable=True)
    img = models.ImageField('主图',upload_to='tags',null=True,blank=True)
    code = models.CharField('编码', max_length=32, null=True, blank=True)
    name = models.CharField('名称', max_length=12)
    reorder = models.SmallIntegerField('排序', default=0)
    is_valid = models.BooleanField('是否有效', default=True)

    created_at = models.DateTimeField('创建时间', auto_now_add=True)
    updated_at = models.DateTimeField('修改时间', auto_now=True)

    class Meta:
        db_table = 'mall_tag'


class Product(models.Model):
    """商品"""
    uid = models.UUIDField('商品ID', default=uuid.uuid4)
    name = models.CharField('商品名称', max_length=128)
    desc = models.CharField('简单描述', max_length=256, null=True, blank=True)
    content = models.TextField('商品描述')
    types = models.SmallIntegerField('商品类型', choices=constants.SLIDER_TYPES_CHOICES,
                                     default=constants.PRODUCT_TYPE_ACTUALL)
    price = models.IntegerField('兑换价格(积分兑换)')
    origin_paice = models.FloatField('原价')
    img = models.ImageField('主图', upload_to='product')
    buy_link = models.CharField('购买链接', max_length=256, null=True, blank=True)
    reorder = models.SmallIntegerField('排序', default=0)
    status = models.SmallIntegerField('商品状态', default=constants.PRODUCT_STATUS_LOST,
                                      choices=constants.PRODUCT_STATUS_CHOICES)
    sku_count = models.IntegerField('库存', default=0)
    remain_count = models.IntegerField('剩余库存', default=0)
    view_count = models.IntegerField('浏览次数', default=0)
    score = models.FloatField('商品评分', default=10)
    is_valid = models.BooleanField('是否有效', default=True)
    created_at = models.DateTimeField('创建时间', auto_now_add=True)
    updated_at = models.DateTimeField('修改时间', auto_now=True)

    class Meta:
        db_table = 'mall_product'
        ordering = ['-reorder']
