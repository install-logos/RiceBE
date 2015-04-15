from django.db import models

# Create your models here.

class Rice(models.Model):
   name = models.CharField(max_length=200)
   program = models.CharField(max_length=300)
   description = models.CharField(max_length=500)
   cover = models.URLField()
   pic1 = models.URLField()
   pic2 = models.URLField()
   pic3 = models.URLField()
   pic4 = models.URLField()
   author = models.URLField()
   upstream = models.URLField()
   version = models.CharField(max_length=50)
