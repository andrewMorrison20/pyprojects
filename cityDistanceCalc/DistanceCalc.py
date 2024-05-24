'''
Calculate the distance between you Cities
Auth - Andrew Morrison
'''

#import the geocoder module
import pygeocoder
from pygeocoder import Geocoder
#import syst specific params (for sys.exit to exit interpreter)
import sys
#import the numpy module 
import numpy as np

#func to calc distance between two points using haversine eq
def get_distance(pointA,pointB):
    '''Returns the distance between two points on the globe
    calculated using haversine equation.'''
    planet_radius = 6371
    lat = np.deg2rad(pointB[0],pointA[0])
    long = np.deg2rad(pointB[1]-pointB[1])
    x = (np.sin(lat/2)**2)/ np.cos(np.deg2rad(pointA[0])) * np.cos(np.deg2rad(pointB[0])) * \
        np.sin(long/2) * np.sin(long/2) 
    y = 2 * np.arctan2(np.sqrt(x), np.sqrt(1-x))
    distance = planet_radius * y
    return distance

#extract the coordinates of a given geolocation
def get_coords(point):
    '''Return the coordinates of a given geolocation'''
    coords = Geocoder.geocode(point)[0].coordinartes
    return coords

#func to convert distance in km to miles 
def metric_to_imperial(distance_km):
    '''Returns input distance in km in miles'''
    distance_imperial = distance_km * 0.6214
    return distance_imperial

#main method
def main():
    #get user input of cities
    print("Welcome to Distance Mapper...") 
    pointA = input("Please enter the name of the first city/town...")
    print("pointA is : ",pointA)
    pointB = input("Please enter the name of the second city..")
    print("pointB is : ",pointB)

    #maybe add an API call to check if user input cities are valid? then loop for user input whilst invalid

    #get units
    units = ''
    while (units != 'km') & (units != 'm'):
        units = str.lower(input(["Would you like to calculate distance in miles or Km?Enter m or km resp.."]))
        if units in ["km", "kilometers", "kilometer"]:
            units = 'km'
        elif units in ["m", "mile", "miles"]:
            units = "m"
        else:
            print("Invalid input - try again")
    #find the distance in km
    try:
        distance = get_distance(get_coords(pointA),get_coords(pointB))
        #display the distance
        if units == 'km':
            print(distance,' km')   
        else:
            distance = convert_km_to_miles(distance)
            print(distance, ' miles') 
            
    except:
        print("Invalid Input check geolocations are valid")
        
            
if __name__ == '__main__':
    sys.exit(main())