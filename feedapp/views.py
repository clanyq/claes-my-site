from django.shortcuts import render, render_to_response


from feedapp.models import News, Press, Image



def index(request):
    latest_press_list = Press.objects.order_by('-pubdate')[:3]
    latest_news_list = News.objects.order_by('-pubdate')[:3]


    return render(request, 'index.html', {'output_press': latest_press_list,
                                          'output_news': latest_news_list})



def all_news(request):
    news = News.objects.order_by('-pubdate')[:5]

    return render(request, 'all_news.html', {'news': news})


def press(request):
    press = Press.objects.order_by('-pubdate')[:5]

    return render(request, 'press.html', {'press': press})


def show_news(request, news_name_slug):
    slug = News.objects.get(slug=news_name_slug)

    return render(request, 'news.html', {'news': slug})



































