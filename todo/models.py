from django.db import models
from django.contrib.auth.models import User
from django.db.models import DateTimeField

class Note(models.Model):
    owner = models.ForeignKey(User, on_delete = models.CASCADE)
    title = models.CharField(max_length=50)
    note = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.title
    


