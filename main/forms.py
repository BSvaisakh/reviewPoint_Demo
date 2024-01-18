from django import forms
from . models import *

#movoie add form

class Movieform(forms.ModelForm):
    class Meta:
        model = Movie
        fields = ("name","director","cast","description","release_date","image")