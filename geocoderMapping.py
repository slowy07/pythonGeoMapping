import geocoder


location = "Rumah Sakit Umum Daerah Langsa,Langsa, Aceh"
loc = geocoder.osm(location)

latlng = [loc.lat, loc.lng]
print(latlng)
