import folium
from classes import StopNode
from data import edges_dict, nodes_dict
import streamlit as st
from streamlit_folium import st_folium


# in-sequence ordered list of StopNodes with attributes: stop_name, stop_lat, stop_lon
stop_nodes = list(nodes_dict.values())

coord = (stop_nodes[0].lat, stop_nodes[0].lon)
m = folium.Map(location=(coord))

for stop in stop_nodes:
    folium.Marker(
        location=[stop.lat, stop.lon],
        popup=f"{stop.name}",
        # icon=folium.Icon(icon="cloud"),
    ).add_to(m)

# print(coords)
#m.save("index.html")
st_data = st_folium(m, width=900)