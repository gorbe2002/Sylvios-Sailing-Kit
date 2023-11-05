import folium
import requests
import math
import streamlit as st
from streamlit_folium import st_folium

# function to use OpenWeatherMap API:
def get_weather_data(city):
    BASE_URL = "https://api.openweathermap.org/data/2.5/weather?"
    API_KEY = open("key", 'r').read()
    url = BASE_URL + "&appid=" + API_KEY + "&q=" + city
    response = requests.get(url).json()
    return response

# Haversine formula (calculates the shortest distance between two points on the surface of a sphere):
def haversine_distance(lat1, lon1, lat2, lon2):
    # convert latitude and longitude from degrees to radians
    lat1, lon1, lat2, lon2 = map(math.radians, [lat1, lon1, lat2, lon2])
    
    dlon = lon2 - lon1 
    dlat = lat2 - lat1 
    a = math.sin(dlat/2)**2 + math.cos(lat1) * math.cos(lat2) * math.sin(dlon/2)**2
    c = 2 * math.atan2(math.sqrt(a), math.sqrt(1-a))
    
    # radius of  Earth (in km)
    radius = 6371.0
    
    distance = radius * c
    return distance

# title of website:
st.title("Welcome to Sylvio's Sailing Kit!")
st.divider()
start_location = st.selectbox('Select a starting port in one of the following locations', ["Newark, USA", "Paramaribo, Suriname", "Lisbon, Portugal", "Algeciras, Spain"])

# given ports latitudes and longitudes [lat, lon]
newarkLatLon = [40.685790, -74.162510]
# rioLatLon = [-22.898360, -43.180960]
paramariboLatLon = [5.811784, -55.169924]
lisbonLatLon = [38.701191, -9.165530]
algecirasLatLon = [36.126930, -5.443430]

# keep track of coordinates to use for Haversine formula
start_lat = None
start_lon = None
end_lat = None
end_lon = None

# change map depending on the starting location chosen:
if start_location == "Newark, USA":
    start_lat, start_lon = newarkLatLon[0], newarkLatLon[1]
    my_map = folium.Map(location=newarkLatLon, zoom_start=13)
    folium.Marker(location=newarkLatLon, popup="Port Newark Container Terminal", tooltip="Port Newark Container Terminal").add_to(my_map)
    # folium.Marker(location=[-22.898360, -43.180960], popup="Porto do Rio de Janiero", tooltip="Porto do Rio de Janiero").add_to(my_map)
    folium.Marker(location=[5.811784, -55.169924], popup="Jules Sedney Harbour", tooltip="Jules Sedney Harbour").add_to(my_map)
    folium.Marker(location=[38.701191, -9.165530], popup="Port of Lisbon", tooltip="Port of Lisbon").add_to(my_map)
    folium.Marker(location=[36.126930, -5.443430], popup="Port of Algeciras", tooltip="Port of Algeciras").add_to(my_map)
    st_data = st_folium(my_map, width=700)
elif start_location == "Paramaribo, Suriname":
    start_lat, start_lon = paramariboLatLon[0], paramariboLatLon[1]
    my_map = folium.Map(location=paramariboLatLon, zoom_start=15)
    folium.Marker(location=[40.685790, -74.162510], popup="Port Newark Container Terminal", tooltip="Port Newark Container Terminal").add_to(my_map)
    # folium.Marker(location=rioLatLon, popup="Porto do Rio de Janiero", tooltip="Porto do Rio de Janiero").add_to(my_map)
    folium.Marker(location=paramariboLatLon, popup="Jules Sedney Harbour", tooltip="Jules Sedney Harbour").add_to(my_map)
    folium.Marker(location=[38.701191, -9.165530], popup="Port of Lisbon", tooltip="Port of Lisbon").add_to(my_map)
    folium.Marker(location=[36.126930, -5.443430], popup="Port of Algeciras", tooltip="Port of Algeciras").add_to(my_map)
    st_data = st_folium(my_map, width=700)
elif start_location == "Lisbon, Portugal":
    start_lat, start_lon = lisbonLatLon[0], lisbonLatLon[1]
    my_map = folium.Map(location=lisbonLatLon, zoom_start=15)
    folium.Marker(location=[40.685790, -74.162510], popup="Port Newark Container Terminal", tooltip="Port Newark Container Terminal").add_to(my_map)
    # folium.Marker(location=[-22.898360, -43.180960], popup="Porto do Rio de Janiero", tooltip="Porto do Rio de Janiero").add_to(my_map)
    folium.Marker(location=[5.811784, -55.169924], popup="Jules Sedney Harbour", tooltip="Jules Sedney Harbour").add_to(my_map)
    folium.Marker(location=lisbonLatLon, popup="Port of Lisbon", tooltip="Port of Lisbon").add_to(my_map)
    folium.Marker(location=[36.126930, -5.443430], popup="Port of Algeciras", tooltip="Port of Algeciras").add_to(my_map)
    st_data = st_folium(my_map, width=700)
elif start_location == "Algeciras, Spain":
    start_lat, start_lon = algecirasLatLon[0], algecirasLatLon[1]
    my_map = folium.Map(location=algecirasLatLon, zoom_start=15)
    folium.Marker(location=[40.685790, -74.162510], popup="Port Newark Container Terminal", tooltip="Port Newark Container Terminal").add_to(my_map)
    # folium.Marker(location=[-22.898360, -43.180960], popup="Porto do Rio de Janiero", tooltip="Porto do Rio de Janiero").add_to(my_map)
    folium.Marker(location=[5.811784, -55.169924], popup="Jules Sedney Harbour", tooltip="Jules Sedney Harbour").add_to(my_map)
    folium.Marker(location=[38.701191, -9.165530], popup="Port of Lisbon", tooltip="Port of Lisbon").add_to(my_map)
    folium.Marker(location=algecirasLatLon, popup="Port of Algeciras", tooltip="Port of Algeciras").add_to(my_map)
    st_data = st_folium(my_map, width=700)

# ending location
end_location = st.selectbox('Select an ending port in one of the following locations', ["Newark, USA", "Paramaribo, Suriname", "Lisbon, Portugal", "Algeciras, Spain"])

# getting latitude and longitude of end coordinates
if end_location == "Newark, USA":
    end_lat, end_lon = newarkLatLon[0], newarkLatLon[1]
elif end_location == "Paramaribo, Suriname":
    end_lat, end_lon = paramariboLatLon[0], paramariboLatLon[1]
elif end_location == "Lisbon, Portugal":
    end_lat, end_lon = lisbonLatLon[0], lisbonLatLon[1]
elif end_location == "Algeciras, Spain":
    end_lat, end_lon = algecirasLatLon[0], algecirasLatLon[1]

# get weather data based on the selected location:
locationMapping = {
    "Newark, USA": "Newark", 
    # "Rio de Janiero, Brazil": "Rio",
    "Paramaribo, Suriname": "Paramaribo",
    "Lisbon, Portugal": "Lisbon",
    "Algeciras, Spain": "Algeciras"
}
selected_city = locationMapping[start_location]
weather_data = get_weather_data(selected_city)

# extract weather data:
tempKelvin = weather_data['main']['temp']
tempFahrenheit = ((tempKelvin - 273.15) * 9/5 + 32)
tempFeelsLikeKelvin = weather_data['main']['feels_like']
tempFeelsLikeFahrenheit = ((tempFeelsLikeKelvin - 273.15) * 9/5 + 32)
humidity = weather_data['main']['humidity']
windSpeed = weather_data['wind']['speed']
description = weather_data['weather'][0]['description']

# calculate and Haversine formula
distance = haversine_distance(start_lat, start_lon, end_lat, end_lon)
st.subheader(f"Distance between {start_location} and {end_location} is {distance:.2f} km")
st.divider()

# adding destination map with line between both points
st.title("Destination map:")
route_coordinates = [(start_lat, start_lon), (end_lat, end_lon)]
route_map = folium.Map(location=[start_lat, start_lon], zoom_start=4)
route_line = folium.PolyLine(smooth_factor=50, locations=route_coordinates, color='blue', weight=5, opacity=1, tooltip=f"From {start_location} to {end_location}")
route_line.add_to(route_map)
if (start_location == "Newark, USA" or end_location == "Newark, USA"):
    folium.Marker(location=newarkLatLon, popup="Port Newark Container Terminal", tooltip="Port Newark Container Terminal").add_to(route_map)
# if (start_location == "Rio de Janiero, Brazil" or end_location == "Rio de Janiero, Brazil"):
#     folium.Marker(location=rioLatLon, popup="Porto do Rio de Janiero", tooltip="Porto do Rio de Janiero").add_to(route_map)
if (start_location == "Paramaribo, Suriname" or end_location == "Paramaribo, Suriname"):
    folium.Marker(location=paramariboLatLon, popup="Jules Sedney Harbour", tooltip="Jules Sedney Harbour").add_to(route_map)
if (start_location == "Lisbon, Portugal" or end_location == "Lisbon, Portugal"):
    folium.Marker(location=lisbonLatLon, popup="Port of Lisbon", tooltip="Port of Lisbon").add_to(route_map)
if (start_location == "Algeciras, Spain" or end_location == "Algeciras, Spain"):
    folium.Marker(location=algecirasLatLon, popup="Port of Algeciras", tooltip="Port of Algeciras").add_to(route_map)
st_data = st_folium(route_map, width=700)

# display weather data:
st.title(f"Relevant weather data in {start_location}:")
st.write(f"Temperature: {tempFahrenheit:.2f}°F")
st.write(f"Temperature feels like: {tempFeelsLikeFahrenheit:.2f}°F")
st.write(f"Humidity: {humidity}%")
st.write(f"Wind speed: {windSpeed} m/s")
st.write(f"Weather description: {description}")

# SeaWorldle:
# st.header("SeaworldLe")
# st.write('https://github.com/gorbe2002/HackNJIT2023/blob/main/seaWorldLe.php', unsafe_allow_html=True)
