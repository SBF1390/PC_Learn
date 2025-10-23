from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=100)

class Courses(models.Model):
    title = models.CharField(max_length=100)
    short_description = models.CharField(max_length=100)
    description = models.TextField(max_length=199)
    category_id = models.ManyToManyField(
        Category,
        on_delete=models.CASCADE,
        related_name="Category"
    )
    price = models.DecimalField(default=0)
    is_published = models.BooleanField(default=False)
    published_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"title: {self.title} / is_done: {self.is_done}"


class Session(models.Model):
    name = models.CharField(max_length=100)
    content = models.JSONField()
    course = models.ForeignKey(Courses, on_delete=models.CASCADE)

    def __str__(self):
        return f'Session "{self.name}" for Course "{self.course.title}"'