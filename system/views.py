from django.core.paginator import Paginator
from django.db.models import F
from django.shortcuts import render, get_object_or_404

# Create your views here.
from system.models import News
from utils import constants


def news_list(request, template_name='news_list.html'):
    """"""
    page = request.GET.get('page',1)
    page_size = 10
    news = News.objects.filter(types=constants.NEWS_TYPE_NEW,
                               is_valid=True)
    paginator = Paginator(news, page_size)
    """获取某一页的数据"""
    page_data = paginator.get_page(page)
    return render(request, template_name, {

        'page_data':page_data,
    })


def news_detail(request, pk,template_name='news_info.html'):
    """"""
    # new_obj = News.objects.get(pk=pk)
    # for i in new_obj:
    #     print(i.content) get()函数有pk,all()没有pk字段
    new_obj = get_object_or_404(News,pk=pk,is_valid=True)
    print(new_obj)
    """浏览次数加一"""
    new_obj.view_count = F('view_count')+1
    new_obj.save()
    """重新从数据库取数据"""
    new_obj.refresh_from_db()
    return render(request, template_name, {
        'new_obj':new_obj

    })
