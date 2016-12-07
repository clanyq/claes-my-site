from django.shortcuts import render, render_to_response
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

from feedapp.models import News, Press, Image
from feedapp.forms import NewsForm, PressForm, ImageForm


def index(request):
    latest_press_list = Press.objects.order_by('-pubdate')[:3]
    output_press = ', '.join([p.title for p in latest_press_list])

    latest_news_list = News.objects.order_by('-pubdate')[:3]


    return render(request, 'index.html', {'output_press': latest_press_list, 'output_news': latest_news_list})


def user_login(request):

    if request.method == 'POST':

        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(username=username, password=password)

        if user:
            if user.is_active:
                login(request, user)
                return HttpResponseRedirect('/input')
            else:
                return HttpResponse("Your account is disabled.")
        else:

            return HttpResponse("Invalid login details supplied.")

    else:
        return render(request, 'login.html')


def user_logout(request):
    logout(request)
    return HttpResponseRedirect('/')


def news_form(request):
    if request.user.is_authenticated:
        newsform = NewsForm()

        if request.method == 'POST':
            newsform = NewsForm(request.POST)
            if newsform.is_valid():
                newsform.save(commit=True)
                newsform = NewsForm()
            else:
                print(newsform.errors)

        return render(request, 'newsform.html', {'newsform': newsform})
    else:
        return HttpResponseRedirect('/login')

def press_form(request):
    if request.user.is_authenticated:
        pressform = PressForm()

        if request.method == 'POST':
            pressform = PressForm(request.POST)
            if pressform.is_valid():
                pressform.save(commit=True)
                pressform = PressForm()
            else:
                print(pressform.errors)

        return render(request, 'pressform.html', {'pressform': pressform})
    else:
        return HttpResponseRedirect('/login')


def pic_remove(request):
    if request.user.is_authenticated:
        return render(request, 'pic_remove.html')
    else:
        return HttpResponseRedirect('/login')


def pic_upload(request):
    if request.user.is_authenticated:
        # Handle file upload
        if request.method == 'POST':
            form = ImageForm(request.POST, request.FILES)
            if form.is_valid():
                newimg = Image(imgfile = request.FILES['imgfile'])
                newimg.save()
                form = ImageForm()

        else:
            form = ImageForm()

        return render(request, 'pic_upload.html', {'form': form})
    else:
        return HttpResponseRedirect('/login')


def admin_site(request):
    if request.user.is_authenticated:
        return render(request, 'input.html')
    else:
        return HttpResponseRedirect('/login')


def all_news(request):
    news = News.objects.order_by('-pubdate')[:5]

    return render(request, 'all_news.html', {'news': news})


def press(request):
    press = Press.objects.order_by('-pubdate')[:5]

    return render(request, 'press.html', {'press': press})


def show_news(request, news_name_slug):
    print(news_name_slug)

    slug = News.objects.get(slug=news_name_slug)

    return render(request, 'news.html', {'news': slug})



































