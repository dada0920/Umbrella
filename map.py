import googlemaps
import folium
gmaps_key = "AIzaSyDQKxbTt0MrFNH85kTJXzickMD5s88UVaI"
gmaps = googlemaps.Client(key=gmaps_key)

gmaps.geocode('대한민국 서울특별시 강남구 대치2동 514', language='ko')


ff = folium.Map(location = [45.5236, -122.6750])
ff
