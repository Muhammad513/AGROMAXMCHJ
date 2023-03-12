from django.contrib import admin
from .models import*
# Register your models here.




class ProfileAdmin(admin.ModelAdmin):
    list_display = ('id','user','shtat')



admin.site.register(Profile,ProfileAdmin)    

admin.site.register([Shtat,Bolim,Fizlitsa,Narxnoma,Oylar,Qabul,Naryad])