from django.db import models

class Point(models.Model):
    lattitude  = models.CharField(max_length=30)
    longtitude = models.CharField(max_length=30)
    image      = models.ImageField(upload_to="%s:%s" % (lattitude, longtitude))