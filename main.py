import folium
from classes import StopNode
from data import edges_dict, nodes_dict, path_coords
import streamlit as st
from streamlit_folium import st_folium


# # in-sequence ordered list of StopNodes with attributes: stop_name, stop_lat, stop_lon
# stop_nodes = list(nodes_dict.values())

# Hardcoding coordinates: center of the Bay. This is what the map will open on.
coord = (37.812650, -122.360739) 
m = folium.Map(location=(coord))

radius = 50
for id, stop in nodes_dict.items():
    folium.Circle(
        location=[stop.lat, stop.lon],
        radius=radius,
        color="black",
        weight=1,
        fill_opacity=0.7,
        opacity=1,
        fill_color="green",
        fill=False,  # gets overridden by fill_color
        popup=id,
        tooltip=stop.name,
    ).add_to(m)

# for stop in stop_nodes:
#     folium.Marker(
#         location=[stop.lat, stop.lon],
#         popup=f"{stop.name}",
#         # icon=folium.Icon(icon="cloud"),
#     ).add_to(m)

# print(coords)
#m.save("index.html")

folium.PolyLine(
    locations=path_coords,
    color="#FF0000",
    weight=5,
    #tooltip="From Boston to San Francisco",
).add_to(m)

st_data = st_folium(m, width=900)