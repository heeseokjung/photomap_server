from django.shortcuts import render
from django.http import HttpResponse, JsonResponse

def get(request):
    pass

def post(request):
    if request.method == 'POST':
        lattitude = request.POST['lattitude']
        longtitude = request.POST['longtitude']
        image = request.FILES['image']

        p = Point(lattitude, longtitude, image)
        p.save()

        return JsonResponse({'message' : 'SUCCESS'}, status=200)
    else:
        return JsonResponse({'message' : 'INVALID KEY'}, status=400)