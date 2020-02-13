from django.db import models
from django.contrib.auth.models import User

from django.db.models import DateTimeField

class Todo(models.Model):
    owner = models.ForeignKey(User, on_delete = models.CASCADE)
    title = models.CharField(max_length=50, min_length=3)
    todo = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
    


class Status(models.Model):
    todo = models.ForeignKey(Todo, on_delete=models.CASCADE)
    completed = models.BooleanField(default=False)
    date_completed = models.DateTimeField(auto_now_add=True)

