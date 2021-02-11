from django.db import models

def user_directory_path(instance, filename):
    return '%s:%s/%s' % (instance.latitude, instance.longtitude, filename)

class Point(models.Model):
    latitude   = models.CharField(max_length=50)
    longtitude = models.CharField(max_length=50)
    title      = models.CharField(max_length=50)
    content    = models.CharField(max_length=200, null=True)
    image      = models.ImageField(upload_to=user_directory_path)
