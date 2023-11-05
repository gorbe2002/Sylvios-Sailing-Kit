import folium
import requests
import streamlit as st
from streamlit_folium import st_folium

# function to use OpenWeatherMap API:
def get_weather_data(city):
    BASE_URL = "https://api.openweathermap.org/data/2.5/weather?"
    API_KEY = open("key", 'r').read()
    url = BASE_URL + "&appid=" + API_KEY + "&q=" + city
    response = requests.get(url).json()
    return response

# title of website:
st.title("Welcome to Sylvester Smart Sailing!")
st.divider()
location = st.selectbox('Select a port in one of the following locations', ["Newark, USA", "Rio de Janiero, Brazil", "Lisbon, Portugal", "Algeciras, Spain"])

# change map depending on the location chosen:
if location == "Newark, USA":
    newarkLatLon = [40.685790, -74.162510]
    my_map = folium.Map(location=newarkLatLon, zoom_start=13)
    folium.Marker(location=newarkLatLon, popup="Port Newark Container Terminal", tooltip="Port Newark Container Terminal").add_to(my_map)
    folium.Marker(location=[-22.898360, -43.180960], popup="Porto do Rio de Janiero", tooltip="Porto do Rio de Janiero").add_to(my_map)
    folium.Marker(location=[38.701191, -9.165530], popup="Port of Lisbon", tooltip="Port of Lisbon").add_to(my_map)
    folium.Marker(location=[36.126930, -5.443430], popup="Port of Algeciras", tooltip="Port of Algeciras").add_to(my_map)
    st_data = st_folium(my_map, width=700)
elif location == "Rio de Janiero, Brazil":
    rioLatLon = [-22.898360, -43.180960]
    my_map = folium.Map(location=rioLatLon, zoom_start=15)
    folium.Marker(location=[40.685790, -74.162510], popup="Port Newark Container Terminal", tooltip="Port Newark Container Terminal").add_to(my_map)
    folium.Marker(location=rioLatLon, popup="Porto do Rio de Janiero", tooltip="Porto do Rio de Janiero").add_to(my_map)
    folium.Marker(location=[38.701191, -9.165530], popup="Port of Lisbon", tooltip="Port of Lisbon").add_to(my_map)
    folium.Marker(location=[36.126930, -5.443430], popup="Port of Algeciras", tooltip="Port of Algeciras").add_to(my_map)
    st_data = st_folium(my_map, width=700)
elif location == "Lisbon, Portugal":
    lisbonLatLon = [38.701191, -9.165530]
    my_map = folium.Map(location=lisbonLatLon, zoom_start=15)
    folium.Marker(location=[40.685790, -74.162510], popup="Port Newark Container Terminal", tooltip="Port Newark Container Terminal").add_to(my_map)
    folium.Marker(location=[-22.898360, -43.180960], popup="Porto do Rio de Janiero", tooltip="Porto do Rio de Janiero").add_to(my_map)
    folium.Marker(location=lisbonLatLon, popup="Port of Lisbon", tooltip="Port of Lisbon").add_to(my_map)
    folium.Marker(location=[36.126930, -5.443430], popup="Port of Algeciras", tooltip="Port of Algeciras").add_to(my_map)
    st_data = st_folium(my_map, width=700)
elif location == "Algeciras, Spain":
    andalusiaLatLon = [36.126930, -5.443430]
    my_map = folium.Map(location=andalusiaLatLon, zoom_start=15)
    folium.Marker(location=[40.685790, -74.162510], popup="Port Newark Container Terminal", tooltip="Port Newark Container Terminal").add_to(my_map)
    folium.Marker(location=[-22.898360, -43.180960], popup="Porto do Rio de Janiero", tooltip="Porto do Rio de Janiero").add_to(my_map)
    folium.Marker(location=[38.701191, -9.165530], popup="Port of Lisbon", tooltip="Port of Lisbon").add_to(my_map)
    folium.Marker(location=andalusiaLatLon, popup="Port of Algeciras", tooltip="Port of Algeciras").add_to(my_map)
    st_data = st_folium(my_map, width=700)

# get weather data based on the selected location:
locationMapping = {
    "Newark, USA": "Newark", 
    "Rio de Janiero, Brazil": "Rio",
    "Lisbon, Portugal": "Lisbon",
    "Algeciras, Spain": "Algeciras"
}
selected_city = locationMapping[location]
weather_data = get_weather_data(selected_city)

# extract weather data:
tempKelvin = weather_data['main']['temp']
tempFahrenheit = ((tempKelvin - 273.15) * 9/5 + 32)
windSpeed = weather_data['wind']['speed']
description = weather_data['weather'][0]['description']

# display weather data:
st.title(f"Relevant weather data in {location}:")
st.divider()
st.write(f"\tTemperature: {tempFahrenheit:.2f}°F")
st.write(f"\tWind speed: {windSpeed} m/s")
st.write(f"\tWeather description: {description}")

# SeaWorldle:
# st.header("SeaworldLe")
# st.write('https://github.com/gorbe2002/HackNJIT2023/blob/main/seaWorldLe.php', unsafe_allow_html=True)
