from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth import authenticate, login

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


def user_login(request):

    # If the request is a HTTP POST, try to pull out the relevant information.
    if request.method == 'POST':
        # Gather the username and password provided by the user.
        # This information is obtained from the login form.
                # We use request.POST.get('<variable>') as opposed to request.POST['<variable>'],
                # because the request.POST.get('<variable>') returns None, if the value does not exist,
                # while the request.POST['<variable>'] will raise key error exception
        username = request.POST.get('username')
        password = request.POST.get('password')

        # Use Django's machinery to attempt to see if the username/password
        # combination is valid - a User object is returned if it is.
        user = authenticate(username=username, password=password)

        # If we have a User object, the details are correct.
        # If None (Python's way of representing the absence of a value), no user
        # with matching credentials was found.
        if user:
            # Is the account active? It could have been disabled.
            if user.is_active:
                # If the account is valid and active, we can log the user in.
                # We'll send the user back to the homepage.
                login(request, user)
                return HttpResponseRedirect('/feedapp/pressform')
            else:
                # An inactive account was used - no logging in!
                return HttpResponse("Your account is disabled.")
        else:
            # Bad login details were provided. So we can't log the user in.
            print "Invalid login details: {0}, {1}".format(username, password)
            return HttpResponse("Invalid login details supplied.")

    # The request is not a HTTP POST, so display the login form.
    # This scenario would most likely be a HTTP GET.
    else:
        # No context variables to pass to the template system, hence the
        # blank dictionary object...
        return render(request, 'login.html', {})
