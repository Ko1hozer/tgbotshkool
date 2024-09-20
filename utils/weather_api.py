# utils/weather_api.py

import requests
from config import OPENWEATHER_API_KEY

def get_weather(city):
    url = f'http://api.openweathermap.org/data/2.5/weather?q={city}&appid={OPENWEATHER_API_KEY}&units=metric&lang=ru'
    response = requests.get(url)
    data = response.json()
    if data.get('cod') != 200:
        return 'Не удалось получить данные о погоде.'
    weather = data['weather'][0]['description']
    temperature = data['main']['temp']
    wind_speed = data['wind']['speed']
    # Проверка на актировку
    notice = ''
    if temperature <= -25 or wind_speed >= 15:
        notice = '\nВнимание! Возможна актировка.'
    return f'{weather.capitalize()}, температура {temperature}°C, ветер {wind_speed} м/с.{notice}'
