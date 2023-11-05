import datetime as dt
import requests

BASE_URL = "https://api.openweathermap.org/data/2.5/weather?"
API_KEY = open("key", 'r').read()
CITY = "Algeciras"

url = BASE_URL + "&appid=" + API_KEY + "&q=" + CITY

response = requests.get(url).json()
# print(response)

def kelvinToFahrenheit(kelvin):
    return ((kelvin - 273.15) * 9/5 + 32)

tempKelvin = response['main']['temp']
tempFahrenheit = kelvinToFahrenheit(tempKelvin)
tempFeelsLikeKelvin = response['main']['feels_like']
tempFeelsLikeFahrenheit = kelvinToFahrenheit(tempFeelsLikeKelvin)
humidity = response['main']['humidity']
windSpeed = response['wind']['speed']
description = response['weather'][0]['description']

print(f"Temperature in {CITY}: {tempFahrenheit:.2f}°F")
print(f"Temperature in {CITY} feels like: {tempFeelsLikeFahrenheit:.2f}°F")
print(f"Humidity in {CITY}: {humidity}%")
print(f"Wind speed in {CITY}: {windSpeed}m/s")
print(f"Weather description in {CITY}: {description}")