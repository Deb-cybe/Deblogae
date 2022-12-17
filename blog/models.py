from django.db import models
from datetime import datetime

# Create your models here.
class Post(models.Model):
    title=models.CharField(max_length=50)
    desc=models.TextField()
    timeofc=models.DateTimeField(default=datetime.now,blank=True)