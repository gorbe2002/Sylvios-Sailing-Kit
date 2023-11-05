import streamlit as st
import folium

# title:
st.title("Welcome to Sylvester Smart Sailing!")
st.selectbox('Select a location', ["Newark", "Rio", "London"])

# map centered on NJIT:
newarkLatLon = [40.7401, -74.1787]
my_map = folium.Map(location=newarkLatLon, zoom_start=12)
st.write(my_map)

startDate = st.date_input('Enter a starting date')

endDate = st.date_input('Enter an ending date')

st.button('Hit me')
st.checkbox('Check me out')
st.radio('Pick one:', ['nose','ear'])
st.selectbox('Select', [1,2,3])
st.multiselect('Multiselect', [1,2,3])
st.slider('Slide me', min_value=0, max_value=10)
st.select_slider('Slide to select', options=[1,'2'])
st.text_input('Enter some text')
st.number_input('Enter a number')
st.text_area('Area for textual entry')
st.date_input('Date input')
st.time_input('Time entry')
st.file_uploader('File uploader')
st.color_picker('Pick a color')