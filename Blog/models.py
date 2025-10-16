from django.db import models
from datetime import date
from django.db.models.signals import post_save
from django.dispatch import receiver


class Category(models.Model):
    name = models.CharField(max_length=100)


class Blog(models.Model):
    name = models.CharField(max_length=200)
    author = models.CharField(max_length=100)
    content = models.JSONField(default=dict)
    tags = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
    category = models.ManyToManyField(Category, related_name="Blog")

    def __str__(self):
        return f"{self.name} by {self.author}"


class Comment(models.Model):
    blog = models.ForeignKey(Blog, related_name="comments", on_delete=models.CASCADE)
    author = models.CharField(max_length=100)
    text = models.TextField()
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Comment by {self.author} on {self.blog.name}"