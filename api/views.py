from django.shortcuts import render
from django.http import HttpResponse , JsonResponse
from django.shortcuts import render
import requests , json , time
from .models import video_data ,  latest
from django.core.paginator import Paginator


def home(request):
    data = video_data.objects.all()
    if(len(data) == 0):
        time.sleep(10)
    date = latest.objects.all()
    print(len(data))

    return render(request , 'home.html', {'video' : data})


# API to get latest uploaded videos on Youtube .  endpoint - ('get/') , param = ('?page=x')

def get_video_api(request):                          
    data = video_data.objects.all()
    page_number = request.GET.get('page' , 1) 
    if page_number not in [1,2,3] :
        page_number = 1 
    paginator = Paginator(data, 4)
    data = paginator.page(page_number)
    di = dict()
    di['items'] =[] 
    for i in data : 
        te = {}
        te['title'] = i.title
        te['description'] = i.description
        te['thumnail'] = i.thumbnail
        te['published'] = i.published
        di['items'].append(te)

    return JsonResponse(json.dumps(di) , safe=False)


