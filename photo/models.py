from django.db import models

def user_directory_path(instance, filename):
    return '%s:%s/%s' % (instance.lattitude, instance.longtitude, filename)

class Point(models.Model):
    lattitude  = models.CharField(max_length=30)
    longtitude = models.CharField(max_length=30)
    image      = models.ImageField(upload_to=user_directory_path)