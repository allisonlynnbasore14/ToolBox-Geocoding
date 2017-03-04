"""
Geocoding and Web APIs Project Toolbox exercisecd

Find the MBTA stops closest to a given location.

Full instructions are at:
https://sites.google.com/site/sd15spring/home/project-toolbox/geocoding-and-web-apis
"""

from urllib.request import urlopen
import json

GoogleAPI = #####
ExampleGoogleCall = ###

from urllib.request import urlopen
import json
from pprint import pprint


url = ###
response_text = f.read()
response_data = json.loads(str(response_text, "utf-8"))


api_Tstations = ###

lat = response_data["results"][0]["geometry"]["location"]["lat"]
lng = response_data["results"][0]["geometry"]["location"]["lng"]
m = lat,lng


def get_lat_long(place_name):
    """
    Given a place name or address as a string, return a (latitude, longitude) tuple
    with the coordinates of the given place.

    See https://developers.google.com/maps/documentation/geocoding/
    for Google Maps Geocode API URL formatting requirements.
    """
    if place_name == 'Fenway':
        url = "https://maps.googleapis.com/maps/api/geocode/json?address=Fenway%20Park"
        f = urlopen(url)
        response_text = f.read()
        response_data = json.loads(str(response_text, "utf-8"))
        lat = response_data["results"][0]["geometry"]["location"]["lat"]
        lng = response_data["results"][0]["geometry"]["location"]["lng"]
        m = lat,lng
        return m 
    if place_name == 'Museum of Fine Art':
        url = 'https://maps.googleapis.com/maps/api/geocode/json?address=465+Huntington+Ave,+Boston,+MA&key=AIzaSyAox26uPgX2Gv-A0dNWiYN3D3ZuFQ6VKUg'
        f = urlopen(url)
        response_text = f.read()
        response_data = json.loads(str(response_text, "utf-8"))
        lat = response_data["results"][0]["geometry"]["location"]["lat"]
        lng = response_data["results"][0]["geometry"]["location"]["lng"]
        m = lat,lng
        return m 
    if place_name == 'Olin':
        url = 'https://maps.googleapis.com/maps/api/geocode/json?address=1000+Olin+Way,+Needham,+MA&key=AIzaSyAox26uPgX2Gv-A0dNWiYN3D3ZuFQ6VKUg'
        f = urlopen(url)
        response_text = f.read()
        response_data = json.loads(str(response_text, "utf-8"))
        lat = response_data["results"][0]["geometry"]["location"]["lat"]
        lng = response_data["results"][0]["geometry"]["location"]["lng"]
        m = lat,lng
        return m
    if place_name == 'Needham':
        url = 'https://maps.googleapis.com/maps/api/geocode/json?address=1471+Highland+Ave,+Needham,+MA&key=AIzaSyAox26uPgX2Gv-A0dNWiYN3D3ZuFQ6VKUg'
        f = urlopen(url)
        response_text = f.read()
        response_data = json.loads(str(response_text, "utf-8"))
        lat = response_data["results"][0]["geometry"]["location"]["lat"]
        lng = response_data["results"][0]["geometry"]["location"]["lng"]
        m = lat,lng
        return m    
    sep = place_name.split()
    to_add = ''
    for i in sep:
        to_add = to_add + i
        to_add = to_add + '+'
    to_add = to_add[0:-1]
    url = 'https://maps.googleapis.com/maps/api/geocode/json?address='
    Gapikey = 'AIzaSyAox26uPgX2Gv-A0dNWiYN3D3ZuFQ6VKUg'
    url = url + to_add + '&key=' + Gapikey
    f = urlopen(url)
    response_text = f.read()
    response_data = json.loads(str(response_text, "utf-8"))
    lat = response_data["results"][0]["geometry"]["location"]["lat"]
    lng = response_data["results"][0]["geometry"]["location"]["lng"]
    m = lat,lng
    return m



def get_nearest_station(latitude, longitude):
    """
    Given latitude and longitude strings, return a (station_name, distance)
    tuple for the nearest MBTA station to the given coordinates.

    See http://realtime.mbta.com/Portal/Home/Documents for URL
    formatting requirements for the 'stopsbylocation' API.
    """

    MBTAurl = "http://realtime.mbta.com/developer/api/v2/stopsbylocation?api_key=yGzxTxX6v02HXFVwHy1GFA"
    customloc = '&lat=' + str(latitude) + '&lon=' + str(longitude) + "&format=json"
    f = urlopen(MBTAurl+customloc)
    response_text = f.read()
    response_data = json.loads(str(response_text, "utf-8"))
    station = response_data["stop"][0]["stop_name"]
    distanceto = response_data["stop"][0]["distance"]

    #esponse_data["stop"][0]["geometry"]["location"]["lat"]
    return station, distanceto

def find_stop_near():
    """
    Given a place name or address, print the nearest MBTA stop and the
    distance from the given place to that stop.
    """
    input_loc = input('What address or major location would you like to search?   ')
    latlong = get_lat_long(input_loc)
    lat = str(latlong[0])
    lon = str(latlong[1])
    nearest = get_nearest_station(lat,lon) #nearest is a tuple 
    print("The closest station is:   " + str(nearest[0]))
    print("This station is " + str(nearest[1]) + '  miles away.')

#print(get_lat_long('1000 Olin Way, Needham, MA'))

find_stop_near()

#find_stop_near()
#APP_ID = 163709507468731
#APP_SECRET = d794c6b698f11aa343424c4340cdbd6e
#https://graph.facebook.com/walmart/posts/?key=value&access_token=163709507468731|d794c6b698f11aa343424c4340cdbd6e