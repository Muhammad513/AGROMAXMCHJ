from .models import*
from django import forms
import datetime
from .views import*



class ProfileForm(forms.ModelForm):
    class Meta():
        model=Profile
        fields=()