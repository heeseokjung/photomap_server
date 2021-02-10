from django.shortcuts import render
from .models import Point
from django.http import HttpResponse
from django.http import JsonResponse


def get(request):
    pass

def post(request):
        
    if request.method == 'POST':
        
        latitude = request.POST.get('latitude')
        longtitude = request.POST.get('longtitude')
        
        image = request.FILES.get('image')
        print(latitude, longtitude, image)
        p = Point(latitude = latitude, longtitude = longtitude, image = image)
        p.save()

        return HttpResponse(status=200)
        
    else:
        return HttpResponse(status=400)
