import datetime

from django import forms
from newsapp.models import News


class NewsForm(forms.ModelForm):
    title = forms.CharField(max_length=100, help_text='Enter title', required=True)
    body = forms.Textarea()
    pubdate = forms.DateField(required=True, initial=datetime.date.today)

    class Meta:
        model = News
        fields = ('title', 'body', 'pubdate')
