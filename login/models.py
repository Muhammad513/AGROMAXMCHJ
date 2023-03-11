from django.db import models
from PIL import Image
from django.contrib.auth.models import User
import os
from django.db import transaction

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
        return str(self.name)
    

class Fizlitsa(models.Model):
    fname=models.CharField(max_length=20)
    lname=models.CharField(max_length=20)
    oname=models.CharField(max_length=20)

    def __str__(self):
        return f'{self.fname} {self.lname} {self.oname}'
    

class Exemple(models.Model):
    fiz=models.ForeignKey('Fizlitsa',on_delete=models.PROTECT)
    bolim=models.ForeignKey('bolim',on_delete=models.PROTECT)
    name=models.CharField(max_length=20,null=True)
    
    def __str__(self):
        return str(self.fiz)




      

class Shtat(models.Model):
    stf_name=models.CharField(max_length=20)             

    def __str__(self):
        return str(self.stf_name)     