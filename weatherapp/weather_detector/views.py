from django.shortcuts import render
import requests
import urllib.request
import json 

# Create your views here.


def home(request):
    if request.method == 'POST':
        city = request.POST['city']
        
        req = urllib.request.urlopen('http://api.openweathermap.org/data/2.5/weather?q' + city + '&appid=6352ea22a73540f79e583964a1427372').read()
        api_load = json.loads(req)
        
        context = {"country_code": str(api_load['sys']['country']),
                   "coordinate": str(api_load['coord']['lon']) +  ' ' + str(api_load['coord']['lat']),
                   "temp": str(api_load['main']['temp'])+"k",
                   "pressure": str(api_load['main']['pressure']),
                   "humidity": str(api_load['main']['humidity']), 
                   }
        
        return render(request, 'weather_detector/index.html', context)
    
    else:
        city = ' Invalid input'
        return render(request, 'weather_detector/index.html', {'city':city})