from django.contrib.contenttypes.fields import GenericRelation
from django.core.files.images import ImageFile
from django.db import models

# Create your models here.
from accounts.models import User
from mall.models import Product
class Order(models.Model):
    """订单模型"""
    sn = models.CharField("订单编号",max_length=32)

class Comments(models.Model):
    """商品评论"""
    # uid = models.UUIDField('商品ID', default=uuid.uuid4)
    product = models.ForeignKey(Product, on_delete=models.CASCADE,
                                related_name='comments', verbose_name='商品')
    user = models.ForeignKey(User, on_delete=models.CASCADE,
                             related_name='comments', verbose_name='用户')
    is_nick = models.BooleanField('是否匿名', default=True)
    reorder = models.SmallIntegerField('排序', default=0)
    is_top = models.BooleanField('是否置顶', default=True)
    comment_content = models.CharField('评论内容', max_length=256)
    created_at = models.DateTimeField('评论时间', auto_now_add=True)
    updated_at = models.DateTimeField('修改时间', auto_now=True)
    img_list = GenericRelation(ImageFile, verbose_name='评价图',
                               related_query_name='img_list')
    is_valid = models.BooleanField("是否删除", default=True)
    score = models.FloatField('商品评分', default=10.0)
    score_deliver = models.FloatField('配送服务评分', default=10.0)
    score_package = models.FloatField('快递包装评分', default=10.0)
    score_speed = models.FloatField('配送速度评分', default=10.0)

    class Meta:
        db_table = 'mall_comments'
