from django import forms
from pressapp.models import Press


class PressForm(forms.ModelForm):
    title = forms.CharField(max_length=100, help_text='Enter title')
    url = forms.URLField(help_text='Enter url')
    source = forms.CharField(max_length=50, help_text='Enter source')
    pubdate = forms.DateField(help_text='Pick date')

    class Meta:
        model = Press
        fields = ('title', 'url', 'source', 'pubdata')

