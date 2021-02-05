from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from . import models

def get(request):
    pass

def post(request):
    if request.method == 'POST':
        lattitude = request.POST.get('lattitude', '')
        longtitude = request.POST.get('longtitude', '')
        image = request.FILES.get('image', '')

        p = Point(lattitude, longtitude, image)
        p.save()

        return JsonResponse({'message' : 'SUCCESS'}, status=200)
    else:
        return JsonResponse({'message' : 'INVALID KEY'}, status=400)