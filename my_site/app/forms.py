from django import forms
from .models import App

class PersonForm(forms.Form):
    name = forms.CharField(max_length=100,required=True,label='Your Name')
    age = forms.IntegerField(label='Your Age')
    job = forms.CharField(max_length=100,required=False,label='Your Job')

class AppForm(forms.ModelForm):
    class Meta:
        model = App
        fields = ['title','description','is_verified','uploadDate','priority']
        widgets = {
            'uploadDate' : forms.DateInput(attrs={'type':'date'})
        }
        