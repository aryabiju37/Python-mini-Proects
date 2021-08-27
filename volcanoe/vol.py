#Creating a HTML map with python
#use folium - pip install folium, python code to jscript,html and css latitude -90,90 longitude -180,180
import folium
import pandas as pd
#giving in location latitude and longitude and zoom feature

data = pd.read_csv("Volcanoes.txt")
lat = list(data["LAT"])
lon = list(data["LON"])
name = list(data["NAME"])
elev = list(data["ELEV"])

def color_producer(elevation):
    if elevation < 1000:
        return 'green'
    elif 1000<= elevation < 3000:
        return 'orange'
    else:
        return 'red'

fg = folium.FeatureGroup(name = "My Group")
map = folium.Map(location=[38.58,-99.09],zoom_start=6,tiles="Stamen Terrain")
for lt,ln,nm,el in zip(lat,lon,name,elev):
    fg.add_child(folium.ClickForMarker(location=[lt,ln],popup=nm ,icon=folium.Icon(color=color_producer(el))))

map.add_child(fg)
map.save("map1.html")
#add points to the map
