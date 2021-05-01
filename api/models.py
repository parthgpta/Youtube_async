from django.db import models

# Create your models here.

class video_data(models.Model):
    title = models.TextField(null = False) 
    description = models.TextField(null=False) 
    thumbnail = models.TextField()
    published = models.TextField()

class latest(models.Model):
    updated = models.TextField()