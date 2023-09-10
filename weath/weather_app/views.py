from django.shortcuts import render,redirect
import json
import urllib.request
# Create your views here.
def index(request):
    if request.method=='POST':
        city= request.POST['city']
        res= urllib.request.urlopen('http://api.openweathermap.org/data/2.5/weather?q='+city+'&appid=36ad92eb7a6f755c2bff4830f309cb1d').read()
        j_data=json.loads(res)
        data={
            "country_code": str(j_data['sys']['country']),
            "coordinate": 'Lon '+str(j_data['coord']['lon'])+'  Lat '+str(j_data['coord']['lat']),
            "temp": str(round(j_data["main"]["temp"]-273.15,2))+'°C',
            "precep": str(j_data['weather'][0]['main']),
            "icon": j_data['weather'][0]['icon'],
            "pressure": str(j_data['main']['pressure'])+ 'hpa',
            "humidity": str(j_data['main']['humidity'])+ '%',


        }

    else:
        city=''
        data={}
    return render(request,'index.html',{'city':city,'data':data})
