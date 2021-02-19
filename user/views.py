from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from django.http import HttpResponse, JsonResponse
import json
import sys, os
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from photo.models import Point

def signup(request):
    data = json.loads(request.body)

    try:
        if request.method == 'POST':
            username = data['username']
            email = data['email']
            password = data['password']
        
            user = User.objects.create_user(username, email, password)
            user.save()

            return JsonResponse({'message' : 'SUCCESS'}, status=200)
        elif request.method == 'GET':
            # TODO: In case method is GET
            pass
        else:
            return JsonResponse({'message' : 'FAIL'}, status=400)
    except KeyError:
        return JsonResponse({'message' : 'INVALID KEY'}, status=400)

def login(request):
    data = json.loads(request.body)

    try:
        if request.method == 'POST':
            username = data['username']
            email = data['email']
            password = data['password']
            
            user = authenticate(username=username, password=password)
            if user is not None:
                all_markers = Point.objects.all()

                response = HttpResponse(status=200)
                # response.write('message:SUCCESS')
                for marker in all_markers:
                    response.write(marker.latitude + '?')
                    response.write(marker.longtitude + '?')
                    response.write(marker.image.url)
                    response.write('\n')
                
                return response
            else:
                return JsonResponse({'message' : 'FAIL'}, status=400)

        elif request.method == 'GET':
            # TODO: In case method is GET
            pass
        else:
            return JsonResponse({'message' : 'FAIL'}, status=400)
    except KeyError:
        return JsonResponse({'message' : 'INVALID KEY'}, status=400)
