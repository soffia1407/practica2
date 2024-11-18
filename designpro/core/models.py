from django.db import models

class Category(models.Model):
    objects = None
    name = models.CharField(max_length=255)

class Request(models.Model):
    objects = None
    title = models.CharField(max_length=255)
    description = models.TextField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    photo = models.ImageField(upload_to='photos/', max_length=255)
    status = models.CharField(max_length=255, choices=[('new', 'Новая'), ('in_progress', 'Принято в работу'), ('done', 'Выполнено')])
    created_at = models.DateTimeField(auto_now_add=True)
