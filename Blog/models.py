from django.db import models
from datetime import date
from django.db.models.signals import post_save
from django.dispatch import receiver


class Blog(models.Model):
    name = models.CharField(max_length=100)
    author = models.CharField(max_length=100)
    blog = models.TextField()
    image = models.ImageField(null=True)
    date = models.DateField(default=date.today)
