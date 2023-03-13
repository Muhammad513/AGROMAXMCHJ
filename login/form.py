from .models import*
from django import forms
import datetime
from .views import*



class ProfileForm(forms.ModelForm):
    
    
    
    class Meta:
        model=Profile
        fields=('pic','firs_name','last_name')
        widgets={
            'firs_name':forms.TextInput(attrs={'type':'text','class':"form-control"}),
            'last_name':forms.TextInput(attrs={'type':'text','class':"form-control"}),
        }
        def clean_pic(self):
            photo=self.clean_data.get("pic")
            return photo


class NaryadForm(forms.ModelForm):
    
    class Meta:
        model=Naryad
        fields='__all__'    
        

  
