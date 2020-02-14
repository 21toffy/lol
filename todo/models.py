from django.db import models
from django.contrib.auth.models import User
from django.db.models import DateTimeField
from django.utils.text import slugify 
from django.conf import settings
from django.urls import reverse



class Note(models.Model):
    owner = models.ForeignKey(User, on_delete = models.CASCADE)
    title = models.CharField(max_length=50)
    note = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
    slug = models.SlugField(
        default='',
        editable=False,
        
    ) 

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("notes:note_detail", kwargs={"slug": self.slug, "id": self.pk})

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super().save( *args, **kwargs)
    


