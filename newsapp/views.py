from django.shortcuts import render
from django.http import HttpResponse

from newsapp.forms import NewsForm

def index(request):
    return HttpResponse("Testwer")

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