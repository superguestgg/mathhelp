import requests
#Ekaterinburg,RU    
def weathernow(sity):
    s_city = sity
    city_id = 0
    appid = "9af89291e5e450b347fddca88530a82c"
    try:
        res = requests.get("http://api.openweathermap.org/data/2.5/find",
                     params={'q': s_city, 'type': 'like', 'units': 'metric', 'APPID': appid})
        data = res.json()
        cities = ["{} ({})".format(d['name'], d['sys']['country'])
                  for d in data['list']]
        city_id = data['list'][0]['id']
    except Exception as e:
        print("Exception (find):", e)
        pass
    try:
        res = requests.get("http://api.openweathermap.org/data/2.5/weather",
        params={'id': city_id, 'units': 'metric', 'lang': 'ru', 'APPID': appid})
        data = res.json()
        conditionnow=("conditions:", data['weather'][0]['description'])
        tempnow=("temperaturenow:", data['main']['temp'])
        return str(data['main']['temp'])+", "+str(data['weather'][0]['description'])

    except Exception as e:
        print("Exception (weather):", e)
        pass
#print(weathernow())
