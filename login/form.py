from .models import*
from django import forms
import datetime
from .views import*



class ProfileForm(forms.ModelForm):
    
    
    
    class Meta:
        model=Profile
        fields=('firs_name','last_name','pic')
        widgets={
            'firs_name':forms.TextInput(attrs={'type':'text','class':"form-control"}),
            'last_name':forms.TextInput(attrs={'type':'text','class':"form-control"}),
            'pic':forms.TextInput(attrs={'type':'file','class':"account-settings-fileinput"}),
        }