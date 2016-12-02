from django.shortcuts import render
from django.http import HttpResponse

from pressapp.forms import PressForm
from pressapp.models import Press

# def index(request):
#     # Query the database for a list of ALL categories currently stored.
#     # Order the categories by no. likes in descending order.
#     # Retrieve the top 5 only - or all if less than 5.
#     # Place the list in our context_dict dictionary which will be passed to the template engine.
#     # category_list = Press.objects.all
#     # context_dict = {'categories': category_list}
#     form =
#
#     # Render the response and send it back!
#     return render(request, 'base.html', context_dict)

def press_form(request):

    form = PressForm()

    if request.method == 'POST':
        form = PressForm(request.POST)
        if form.is_valid():
            form.save(commit=True)
        else:
            print(form.errors)

    return render(request, 'index.html', {'form': form})


