import time
import requests , json
from api.models import video_data , latest 


def update():
    url = "https://youtube.googleapis.com/youtube/v3/search"
    try :
        latest_date = latest.objects.first().updated
        
    except:
        latest_date = latest(updated = "1970-01-01T00:00:00Z" ) 
        latest_date.save() 
        latest_date = latest.objects.all()[0]
        
    para = {
        'part' : 'snippet' , 
        'maxResults' : 10 ,
        'order' : 'date' ,
        'q' : 'software' ,
        'key' : config.api_key ,
        'publishedAfter'  : latest_date
    }
    
    response = requests.get(url  , params = para)
    d = json.loads(response.text)
    obj = len(d['items'])
    ob = latest.objects.get(id =1)
    ob.updated =  d['items'][obj-1]['snippet']['publishedAt']
    ob.save()
    for i in range(1 , obj+1):
        title = d['items'][i]['snippet']['title']
        description = d['items'][i]['snippet']['description']
        thumbnail = d['items'][i]['snippet']['thumbnails']['high']['url']
        published = d['items'][i]['snippet']['publishedAt']
        a = video_data(id=i , title = title , description = description , thumbnail = thumbnail , published = published)
        a.save()
    print("Done")
