import folium
import pandas as pd

# read data
df1 = pd.read_csv('Volcanoes.csv')
lat = list(df1['LAT'])
lon = list(df1['LON'])
elev = list(df1['ELEV'])
name = list(df1['NAME'])

html = """
<h4> Volcano information </h4>
<a href="https://www.google.com/search?q=%%22%s%%22" target="_blank">%s</a><br>
Height: %s m
"""

# base map using open street map
map1 = folium.Map(location=[lat[0], lon[0]], zoom_start=4)
fg1 = folium.FeatureGroup(name="Test Feature Group")

# place markers and add elevation pop up
for lt, ln, el, nm in zip(lat, lon, elev, name):
    iframe = folium.IFrame(html=html % (nm, nm, el), width=200, height=200)
    fg1.add_child(folium.Marker(location=[lt, ln], popup=folium.Popup(iframe), icon=folium.Icon(color='green')))

map1.add_child(fg1)
map1.save('map1.html')

map2 = folium.Map(location=[lat[0], lon[0]], zoom_start=4, tiles="Mapbox Bright")
map2.save('map2.html')




