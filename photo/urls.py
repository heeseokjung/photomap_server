from django.urls import path
from . import views

urlpatterns = [
    path('get/', view.get),
    path('post/', views.post),
]