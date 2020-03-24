import os
import requests
import json


url = 'https://www.googleapis.com/geolocation/v1/geolocate?key=AIzaSyDQKxbTt0MrFNH85kTJXzickMD5s88UVaI'
data = {
    'considerIp': True,
}

result = requests.post(url, data)

my_location = json.loads(result.text)
print(my_location)
print("lat : ",my_location.get('location').get('lat'))
print("lon : ",my_location.get('location').get('lng'))
