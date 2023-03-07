from django.db import models
from PIL import Image
from django.contrib.auth.models import User

class Profile(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE)
    shtat=models.ForeignKey('shtat',on_delete=models.PROTECT)
    firs_name=models.CharField(max_length=20,blank=True,default='XXXX')
    last_name=models.CharField(max_length=20,blank=True,default='XXXX')
    pic=models.ImageField(upload_to='img',blank=True,null=True,default='default/default.jpg')
    pic_thumbnail=models.ImageField(upload_to='img',blank=True,null=True,default='default/thumbnail.jpg')


    def save(self,*args,**kwargs):
        super().save(*args,**kwargs)
        img=Image.open(self.pic.path)

        if img.height>150 and img.width>150:
            output_size=(50,50)
            img.thumbnail(output_size)
            img.save(self.pic_thumbnail.path)   

    


class Shtat(models.Model):
    stf_name=models.CharField(max_length=20)             

    def __str__(self):
        return str(self.stf_name)     