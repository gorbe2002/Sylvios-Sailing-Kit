import folium
import requests
import streamlit as st
from streamlit_folium import st_folium

# title:
st.title("Welcome to Sylvester Smart Sailing!")
st.divider()
location = st.selectbox('Select a port in one of the following locations', ["Newark, USA", "Rio de Janiero, Brazil", "Lisbon, Portugal"])

# change map depending on the location chosen
if location == "Newark, USA":
    newarkLatLon = [40.685790, -74.162510]
    my_map = folium.Map(location=newarkLatLon, zoom_start=13)
    folium.Marker(location=newarkLatLon, popup="Port Newark Container Terminal", tooltip="Port Newark Container Terminal").add_to(my_map)
    folium.Marker(location=[-22.898360, -43.180960], popup="Porto do Rio de Janiero", tooltip="Porto do Rio de Janiero").add_to(my_map)
    folium.Marker(location=[38.701191, -9.165530], popup="Port of Lisbon", tooltip="Port of Lisbon").add_to(my_map)
    st_data = st_folium(my_map, width=700)
elif location == "Rio de Janiero, Brazil":
    rioLatLon = [-22.898360, -43.180960]
    my_map = folium.Map(location=rioLatLon, zoom_start=15)
    folium.Marker(location=[40.685790, -74.162510], popup="Port Newark Container Terminal", tooltip="Port Newark Container Terminal").add_to(my_map)
    folium.Marker(location=rioLatLon, popup="Porto do Rio de Janiero", tooltip="Porto do Rio de Janiero").add_to(my_map)
    folium.Marker(location=[38.701191, -9.165530], popup="Port of Lisbon", tooltip="Port of Lisbon").add_to(my_map)
    st_data = st_folium(my_map, width=700)
elif location == "Lisbon, Portugal":
    lisbonLatLon = [38.701191, -9.165530]
    my_map = folium.Map(location=lisbonLatLon, zoom_start=15)
    folium.Marker(location=[40.685790, -74.162510], popup="Port Newark Container Terminal", tooltip="Port Newark Container Terminal").add_to(my_map)
    folium.Marker(location=[-22.898360, -43.180960], popup="Porto do Rio de Janiero", tooltip="Porto do Rio de Janiero").add_to(my_map)
    folium.Marker(location=lisbonLatLon, popup="Port of Lisbon", tooltip="Port of Lisbon").add_to(my_map)
    st_data = st_folium(my_map, width=700)

startDate = st.date_input('Enter a starting date')

endDate = st.date_input('Enter an ending date')

# SeaWorldle:
# st.header("SeaworldLe")
# st.write('https://github.com/gorbe2002/HackNJIT2023/blob/main/seaWorldLe.php', unsafe_allow_html=True)
