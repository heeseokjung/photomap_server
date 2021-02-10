from django.shortcuts import render
from django.http import HttpResponse
from .models import Point


def get(request):
    pass

def post(request):
        
    if request.method == 'POST':
        
        latitude = request.POST.get('latitude')
        longtitude = request.POST.get('longtitude')
        image = request.FILES.get('image')
        title = request.POST.get('title')
        content = request.POST.get('content')

        p = Point(latitude, longtitude, title, content, image)
        p.save()

        return HttpResponse(status=200)
    else:
        return HttpResponse(status=400)
