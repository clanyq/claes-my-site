from django.shortcuts import render
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.template import RequestContext

from feedapp.context_processor import image_list
from feedapp.models import News, Press, Image



def index(request):
    latest_press_list = Press.objects.order_by('-pubdate')
    latest_news_list = News.objects.order_by('-pubdate')

    return render(request, 'index.html', {
        'output_press': latest_press_list,
        'output_news' : latest_news_list,
        })


def news_list(request):
    news = News.objects.order_by('-pubdate')
    paginator = Paginator(news, 5)
    page = request.GET.get('page')

    try:
        news = paginator.page(page)
    except PageNotAnInteger:
        news = paginator.page(1)
    except EmptyPage:
        news = paginator.page(paginator.num_pages)

    return render(request, 'news_list.html', {
        'news': news,
        })


def press_list(request):
    press = Press.objects.order_by('-pubdate')
    paginator = Paginator(press, 5)
    page = request.GET.get('page')

    try:
        press = paginator.page(page)
    except PageNotAnInteger:
        press = paginator.page(1)
    except EmptyPage:
        press = paginator.page(paginator.num_pages)

    return render(request, 'press_list.html', {
        'press': press,
        })


def news_detail(request, news_name_slug):
    slug = News.objects.get(slug=news_name_slug)

    return render(request, 'news_detail.html', {
        'news': slug,
        })



































