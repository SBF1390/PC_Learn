from django.db import models


class Courses(models.Model):
    image = models.ImageField()
    title = models.CharField(max_length=100)
    author = models.CharField(max_length=100)
    about = models.TextField(max_length=199)
    is_done = models.BooleanField()

    def __str__(self):
        return f"title: {self.title} / is_done: {self.is_done}"


class Session(models.Model):
    name = models.CharField(max_length=100)
    content = models.JSONField()
    course = models.ForeignKey(Courses, on_delete=models.CASCADE)

    def __str__(self):
        return f'Session "{self.name}" for Course "{self.course.title}"'