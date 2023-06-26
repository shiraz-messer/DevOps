import streamlit as st
from streamlit_folium import st_folium
import folium
import requests


st.title("GIS", anchor=None)

user_input = st.text_input(
    "Enter city name here 👇", placeholder="Example: Tel Aviv-Yafo"
)

center = [0, 0]

m = folium.Map(location=[31.7833, 35.2167], zoom_start=9)


fg = folium.FeatureGroup(name="Markers")
if user_input:
    try:
        # check if hebrew
        flag = "\u0590" <= user_input[0] <= "\u05EA"
        if flag:
            res = requests.get("http://backend:80/he/" + user_input)
            res2 = requests.get("http://logger:8000/" + user_input)
            data = res.json()
            x = data["res"]["x"]
            y = data["res"]["y"]
            center = [x, y]
            fg.add_child(folium.Marker([x, y], zoom_start=16, popup=user_input))
            if x == 0:
                st.warning("Invalid input", icon="⚠️")
        else:
            res = requests.get("http://backend:80/en/" + user_input)
            res2 = requests.get("http://logger:8000/" + user_input)
            data = res.json()
            x = data["res"]["x"]
            y = data["res"]["y"]
            center = [x, y]
            fg.add_child(folium.Marker([x, y], zoom_start=16, popup=user_input))
            if x == 0:
                st.warning("Invalid input", icon="⚠️")
    except:
        st.write("failed")
out = st_folium(
    m,
    feature_group_to_add=fg,
    center=center,
    width=1200,
    height=500,
)
