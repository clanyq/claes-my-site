from django.shortcuts import render
from django.http import HttpResponse

from newsapp.models import News
from newsapp.forms import NewsForm

def index(request):
    latest_press_list = News.objects.order_by('-pubdate')[:5]
    output = ', '.join([p.title for p in latest_press_list])
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