import folium
import json
import os
import dataCSV


overlayData = os.path.join('data/trafficLook.json')

locationData = [3.5781159083168723, 98.67769302278612]
mapping = folium.Map(location=locationData, zoom_start=10)
folium.Marker(location=dataCSV.getCityName('pancabudi'), popup="<strong>place</strong>", tooltip="lahan 1").add_to(mapping)
mapping.save('mapOut/campusPlace.html')