from django.shortcuts import render
from django.http import HttpResponse
from .models import Point


def get(request):
    latitude = request.POST.get('latitude')
    longtitude = request.POST.get('longtitude')

def post(request):     
    if request.method == 'POST':
        latitude = request.POST.get('latitude')
        longtitude = request.POST.get('longtitude')
        image = request.FILES.get('image')
        title = request.POST.get('title')
        content = request.POST.get('content')
        author = request.POST.get('author')

        p = Point(latitude=latitude, 
                  longtitude=longtitude, 
                  title=title, 
                  content=content,
                  author=author,
                  image=image)
        p.save()  

        print('path: %s' % p.image.path)

        return HttpResponse(status=200)
    else:
        return HttpResponse(status=400)
