from django.shortcuts import render, render_to_response
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.template import RequestContext
from django.core.urlresolvers import reverse
from django.conf import settings
from django.core.files.storage import FileSystemStorage


from feedapp.models import News, Press, Document
from feedapp.forms import NewsForm, PressForm, DocumentForm

@login_required()
def news_form(request):
    newsform = NewsForm()

    if request.method == 'POST':
        newsform = NewsForm(request.POST)
        if newsform.is_valid():
            newsform.save(commit=True)
            newsform = NewsForm()
        else:
            print(newsform.errors)

    return render(request, 'newsform.html', {'newsform': newsform})


def index(request):
    latest_press_list = Press.objects.order_by('-pubdate')[:3]
    output_press = ', '.join([p.title for p in latest_press_list])

    latest_news_list = News.objects.order_by('-pubdate')[:3]


    return render(request, 'index.html', {'output_press': latest_press_list, 'output_news': latest_news_list})

@login_required()
def input_form(request):
    pressform = PressForm()
    newsform = NewsForm()
    picform = DocumentForm(request.POST, request.FILES)

    if request.method == 'POST':
        pressform = PressForm(request.POST)
        newsform = NewsForm(request.POST)
        if pressform.is_valid():
            pressform.save(commit=True)
            pressform = PressForm()
        elif newsform.is_valid():
            newsform.save(commit=True)
            newsform = PressForm()
        elif picform.is_valid():
            picform = Document(docfile=request.FILES['docfile'])
            picform.save()
            picform = DocumentForm()
        else:
            print(pressform.errors)

    return render(request, 'input.html', {'pressform': pressform, 'newsform': newsform, 'picform': picform})


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

@login_required()
def pic_upload(request):
    # Handle file upload
    if request.method == 'POST':
        form = DocumentForm(request.POST, request.FILES)
        if form.is_valid():
            newdoc = Document(docfile = request.FILES['docfile'])
            newdoc.save()
            form = DocumentForm()

    else:
        form = DocumentForm()

    return render(request, 'pic_upload.html',{'form': form},

    )


@login_required()
def admin_site(request):
    return render(request, 'input.html')


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
































