from django.shortcuts import render, render_to_response


from feedapp.models import News, Press, Image



def index(request):
    latest_press_list = Press.objects.order_by('-pubdate')
    latest_news_list = News.objects.order_by('-pubdate')
    image = Image.objects.all()


    return render(request, 'index.html',{
                                            'output_press': latest_press_list,
                                            'output_news': latest_news_list,
                                            'images': image,
                                        })


def news_list(request):
    news = News.objects.order_by('-pubdate')
    image = Image.objects.all()

    return render(request, 'news_list.html', {
                                                'news': news,
                                            })


def press_list(request):
    press = Press.objects.order_by('-pubdate')
    image = Image.objects.all()

    return render(request, 'press_list.html', {
                                                    'press': press,
                                                })


def news_detail(request, news_name_slug):
    slug = News.objects.get(slug=news_name_slug)
    image = Image.objects.all()

    return render(request, 'news_detail.html', {
                                                    'news': slug, 
                                                })



































