from django.db import models

class Point(models.Model):
    lattitude  = models.CharField(max_length=30)
    longtitude = models.CharField(max_length=30)
    image      = models.ImageField(upload_to='%s/%s' % (lattitude, longtitude)) # lattitude와 longtitude를 to_string으로 바꿔서 정규표현식형태로 넣어야함