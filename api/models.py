from django.db import models

class Myapi(models.Model):
    title = models.CharField(max_length=50, null=True, blank=True)
    img=models.ImageField(upload_to='image/', null=True, blank=True)
    img2=models.ImageField(upload_to='image/', null=True, blank=True)
    price=models.CharField(max_length=20, null=True, blank=True)
    desc= models.TextField( null=True, blank=True)
    rating =models.IntegerField( null=True, blank=True)
# Create your models here.
