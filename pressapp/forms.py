import datetime

from django import forms
from pressapp.models import Press


class PressForm(forms.ModelForm):
    title = forms.CharField(max_length=100, help_text='Enter title', required=True)
    url = forms.URLField(help_text='Enter url', required=True)
    source = forms.CharField(max_length=50, help_text='Enter source', required=True)
    pubdate = forms.DateField(required=True, initial=datetime.date.today)

    class Meta:
        model = Press
        fields = ('title', 'url', 'source', 'pubdate')

