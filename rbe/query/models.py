from django.db import models

# Create your models here.

class Package(models.Model):
   name = models.CharField(max_length=200)
   program = models.CharField(max_length=300)
   description = models.CharField(max_length=500)
   cover = models.URLField()
   pic1 = models.URLField(blank=True)
   pic2 = models.URLField(blank=True)
   pic3 = models.URLField(blank=True)
   pic4 = models.URLField(blank=True)
   author = models.CharField(max_length=100, blank=True)
   upstream = models.URLField()
   version = models.CharField(max_length=50, blank=True)
   
   def __str__(self):
       return self.name
