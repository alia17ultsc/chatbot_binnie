import requests

def getweather(city):
    url='https://api.openweathermap.org/data/2.5/weather?q='+city+'&units=metric&lang=en&appid=79d1ca96933b0328e1c7e3e7a26cb347'
    weather_info=requests.get(url).json()
    temp=round(weather_info['main']['temp'])
    feel_temp=round(weather_info['main']['feels_like'])
    description=weather_info['weather'][0]['description']
    wind_speed=round(weather_info['wind']['speed'], 2)
    weather_str=f'Temperature {temp}\nFeels like {feel_temp}\n{description}\nWind speed {wind_speed}'
    print(weather_str)
    return weather_str

#getweather('Sharm El-Sheikh')
#getweather('Cairo')
#getweather('Minsk')