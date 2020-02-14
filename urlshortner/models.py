from django.db import models

# Create your models here.

import random, string
def randomword(length):
   letters = string.ascii_lowercase
   return ''.join(random.choice(letters) for i in range(length))

class Link(models.Model):
  attach  = models.CharField(max_length=100)
  niickname = models.CharField(max_length=20)
  url= models.URLField(max_length=200)

  def save(self,*args,**kwargs):
    self.attach = randomword(10)
    super(Link,self).save(*args,**kwargs)

  def __str__(self):
    return self.niickname +' '+ self.attach