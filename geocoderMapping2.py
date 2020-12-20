import geocoder
import folium


location = "Rumah Sakit Umum Daerah Langsa,Langsa, Aceh"
loc = geocoder.osm(location)

latlng = [loc.lat, loc.lng]


mapping = folium.Map(location=latlng, zoom_start=20)
mapping.add_child(folium.Marker(location=latlng, popup=loc.address, icon = folium.Icon(color='blue')))
mapping.save('mapOut/geocoderMapping2.html')