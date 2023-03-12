from django.db import models
from PIL import Image
from django.contrib.auth.models import User
import os
from django.db import transaction
from .choices import*

def get_image_path(instance,filename):
    return os.path.join('img', str(instance.user.id),filename)


class Profile(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE,unique=True)
    shtat=models.ForeignKey('shtat',on_delete=models.PROTECT)
    firs_name=models.CharField(max_length=20,blank=True,default='XXXX')
    last_name=models.CharField(max_length=20,blank=True,default='XXXX')
    pic=models.ImageField(upload_to=get_image_path,default='img/default.jpg')
        
   
    

class Bolim(models.Model):
    name=models.CharField(max_length=20)


    def __str__(self):
        return str(self.id)
    

class Fizlitsa(models.Model):
    bolim=models.ForeignKey('bolim',on_delete=models.PROTECT,null=True)
    fname=models.CharField(max_length=20)
    lname=models.CharField(max_length=20)
    oname=models.CharField(max_length=20)
    birth=models.DateField(null=True)
    jins=models.CharField(choices=jins,max_length=20,null=True)
    jshir=models.CharField(max_length=14,null=True)
    pasport=models.CharField(max_length=9,null=True)

    def __str__(self):
        return f'{self.fname} {self.lname} {self.oname}'
    

class Qabul(models.Model):
    fizlitsa=models.ForeignKey('Fizlitsa',on_delete=models.PROTECT)
    bolim=models.ForeignKey('bolim',on_delete=models.PROTECT)
    shtat=models.ForeignKey('shtat',on_delete=models.PROTECT)
    
    
    def __str__(self):
        return str(self.fizlitsa)

    


class Narxnoma(models.Model):
    nomi=models.CharField(max_length=20)
    narxi=models.FloatField()

    def __str__(self):
        return str(self.nomi)

      

class Shtat(models.Model):
    stf_name=models.CharField(max_length=20)             

    def __str__(self):
        return str(self.stf_name)     
    

class Oylar(models.Model):
    name=models.CharField(max_length=20)

    def __str__(self):
        return str(self.name)


class Naryad(models.Model):
    bolim=models.ForeignKey('bolim',on_delete=models.PROTECT,null=True)
    oy=models.ForeignKey('Oylar',on_delete=models.PROTECT,null=True)
    hodim=models.ForeignKey('Fizlitsa',on_delete=models.PROTECT,null=True)
    narxnoma=models.ForeignKey('Narxnoma',on_delete=models.PROTECT,null=True)
    miqdor=models.FloatField(null=True)
    summa=models.FloatField(null=True)

    def __str__(self):
        return str(self.hodim)


    def save(self,*args,**kwargs):
        self.summa=round((self.narxnoma.narxi*self.miqdor),1)
        super().save(*args,**kwargs)