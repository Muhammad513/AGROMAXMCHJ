from django.urls import path,include
from .views import loginPage,logout


urlpatterns = [
    path('',loginPage,name='login'),
    path('logout/',logout,name='logout'),
]
