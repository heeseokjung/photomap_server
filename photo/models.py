from django.db import models
import datetime

def user_directory_path(instance, filename):
    extension = ''
    for i in range(len(filename)):
        if filename[i] == '.':
            extension = filename[i:]
    filename = str(datetime.datetime.now()) + extension
    return '%s:%s/%s' % (instance.latitude, instance.longtitude, filename)

class Point(models.Model):
    latitude   = models.CharField(max_length=50)
    longtitude = models.CharField(max_length=50)
    title      = models.CharField(max_length=50)
    content    = models.CharField(max_length=200, null=True)
    author     = models.CharField(max_length=20)
    image      = models.ImageField(upload_to=user_directory_path)

    def __str__(self):
        return self.latitude + ':' + self.longtitude