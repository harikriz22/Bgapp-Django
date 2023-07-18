from django.forms import forms
from . models import Productss, UsrProfile, Newsfeed
from django.forms import ModelForm


class AdminProduct(ModelForm):
    class Meta:
        model = Productss
        fields = '__all__'


class Adnewz(ModelForm):
    class Meta:
        model = Newsfeed
        fields = '__all__'
