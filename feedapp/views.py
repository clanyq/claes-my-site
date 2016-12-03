from django.shortcuts import render
from django.http import HttpResponse

from feedapp.models import News, Press
from feedapp.forms import NewsForm, PressForm

def index(request):
    latest_press_list = News.objects.order_by('-pubdate')[:5]
    output = ' - '.join([p.title for p in latest_press_list])
    return HttpResponse(output)

def news_form(request):

    form = NewsForm()

    if request.method == 'POST':
        form = NewsForm(request.POST)
        if form.is_valid():
            form.save(commit=True)
            form = NewsForm()
        else:
            print(form.errors)

    return render(request, 'newsform.html', {'form': form})


def index(request):
    latest_press_list = Press.objects.order_by('-pubdate')[:5]
    output_press = ', '.join([p.title for p in latest_press_list])
    latest_news_list = News.objects.order_by('-pubdate')[:5]
    output_news = ', '.join([p.title for p in latest_news_list])
    return HttpResponse(output_news + "---------"+ output_press)

def press_form(request):

    form = PressForm()

    if request.method == 'POST':
        form = PressForm(request.POST)
        if form.is_valid():
            form.save(commit=True)
            form = PressForm()
        else:
            print(form.errors)

    return render(request, 'pressform.html', {'form': form})
