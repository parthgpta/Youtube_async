from django.shortcuts import render
from django.http import HttpResponse , JsonResponse
from django.shortcuts import render
import requests , json , time
from .models import video_data ,  latest


def home(request):
    data = video_data.objects.all()
    if(len(data) == 0):
        time.sleep(10)
    date = latest.objects.all()
    print(len(data))

    return render(request , 'home.html', {'video' : data})

