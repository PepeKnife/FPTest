from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class User(AbstractUser):
    pass

class abt_description(models.Model):
    name = models.CharField(max_length=50, default="description")
    text = models.TextField(max_length=400)

class abt_carousel(models.Model):
    num = models.IntegerField(default=1)
    owner = models.CharField(max_length=100)
    text = models.TextField(max_length=300)

class writings(models.Model):
    name = models.CharField(max_length=50)
    text = models.TextField(max_length=500)

class paints(models.Model):
    name = models.CharField(max_length=50)
    paint_img = models.ImageField(upload_to="paints", null=True, blank=True)