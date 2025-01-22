from django.shortcuts import render,redirect
from django.contrib import messages
import requests


# Create your views here.

def home(request):
    if 'city' in request.POST:
         city = request.POST['city']
    else:
         city = 'ahmedabad'     
    
    url = f'https://api.weatherapi.com/v1/current.json?key=f3020f6467aa41e5a5c110122240107&q={city}&aqi=no'
    timeout = 10

    try:
        data = requests.get(url,timeout=timeout).json()
         
        citytemp = data['current']['temp_c']
        citytime = data['location']['localtime']
        feelslike = data['current']['feelslike_c']
        cityname = data['location']['name']
        region = data['location']['region']
        country = data['location']['country']
        humidity = data['current']['humidity']
        UV_index = data['current']['uv']
        wind_speed = data['current']['wind_kph']
        wind_dir = data['current']['wind_dir']
        weather_con = data['current']['condition']['text']
        weather_img = data['current']['condition']['icon']
         
        context = {'citytemp':citytemp, 'citytime':citytime, 'feelslike':feelslike, 'cityname':cityname, 'region':region, 'country':country, 'humidity':humidity, 'UV_index':UV_index, 'wind_speed':wind_speed, 'wind_dir':wind_dir, 'weather_con':weather_con, 'weather_img':weather_img }

        return render(request,'home.html',context)
    
    except KeyError:
        exception_of_location = True
        context = {'exception_of_location':exception_of_location}
        return render(request,'home.html',context)
    
    except (requests.ConnectionError,requests.Timeout):
        exception_of_internet = True
        context = {'exception_of_internet':exception_of_internet}
        # messages.error(request,'no internet')
        return render(request,'home.html',context)
        
