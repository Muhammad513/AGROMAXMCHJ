from django.db import models
from PIL import Image
from django.contrib.auth.models import User
import os
from django_resized import ResizedImageField
from django.db import transaction

def get_image_path(instance,filename):
    return os.path.join('img', str(instance.user.id),filename)
def get_image_path_1(instance,filename):
    return os.path.join('img', str(instance.user.first_name),filename)

def get_image_path_2(instance,filename):
    return os.path.join('img', str(instance.user.last_name),filename)        




class Profile(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE,unique=True)
    shtat=models.ForeignKey('shtat',on_delete=models.PROTECT)
    firs_name=models.CharField(max_length=20,blank=True,default='XXXX')
    last_name=models.CharField(max_length=20,blank=True,default='XXXX')
    pic=models.ImageField(upload_to=get_image_path,default='img/default.jpg')
        
   
    







      

class Shtat(models.Model):
    stf_name=models.CharField(max_length=20)             

    def __str__(self):
        return str(self.stf_name)     