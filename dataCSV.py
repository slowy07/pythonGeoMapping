import pandas as pd
import csv
import geocoder

csvFile = ['ccampusName', 'long', 'lat']
csvData = pd.read_csv('data/campusLocation.csv')

locationData = 'jalan bakti luhur, medan'
get_location = geocoder.osm(locationData)
#print(get_location.lat, get_location.lng)


def getCityName(campusName):
    getCityNameData = csvData[csvData['campusName'] == str(campusName.capitalize())]
    longi = getCityNameData['long']
    lati = getCityNameData['lat']
    return longi,lati

print(getCityName('PancabudiGila'))
