from django.urls import path,include
from .views import loginPage,logoutUser,setting


urlpatterns = [
    path('',loginPage,name='login'),
    path('logout/',logoutUser,name='logout'),
    path('setting',setting,name='setting'),
]
