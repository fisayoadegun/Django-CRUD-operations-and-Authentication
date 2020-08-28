from django import forms
from django.forms import ModelForm
from .models import Flower
class MyForm(forms.ModelForm):
    class Meta:
        model = Flower
        fields = "__all__"
    # title = forms.CharField(label='Title',
    #                         widget= forms.TextInput(attrs={'class': 'form-control '}))
