from django.db.models import F
from django.shortcuts import render, get_object_or_404

# Create your views here.
from system.models import News
from utils import constants


def news_list(request, template_name='news_list.html'):
    """"""
    news = News.objects.filter(types=constants.NEWS_TYPE_NEW,
                               is_valid=True)
    return render(request, template_name, {
        'news_list': news
    })


def news_detail(request, pk,template_name='news_info.html'):
    """"""
    new_obj = get_object_or_404(News,pk=pk,is_valid=True)
    """浏览次数加一"""
    new_obj.view_count = F('view_count')+1
    new_obj.save()
    """重新从数据库取数据"""
    new_obj.refresh_from_db()
    return render(request, template_name, {
        'new_obj':new_obj

    })
