import folium
import pandas as pd

def elev_color(elev):
    if elev < 1000:
        return 'green'
    elif elev < 3000:
        return 'orange'
    else:
        return 'red'

# read data
df_vol = pd.read_csv('Volcanoes.csv')
lat = list(df_vol['LAT'])
lon = list(df_vol['LON'])
elev = list(df_vol['ELEV'])
name = list(df_vol['NAME'])

html = """
<h4> Volcano information </h4>
<a href="https://www.google.com/search?q=%%22%s%%22" target="_blank">%s</a><br>
Height: %s m
"""

# base map using open street map
map1 = folium.Map(location=[lat[0], lon[0]], zoom_start=3)
fg_vol = folium.FeatureGroup(name="Volcanoes")

# place markers and add elevation pop up
for lt, ln, el, nm in zip(lat, lon, elev, name):
    # add link for google search
    iframe = folium.IFrame(html=html % (nm, nm, el), width=200, height=200)
    # add position marker
    fg_vol.add_child(folium.Marker(location=[lt, ln], popup=folium.Popup(iframe), icon=folium.Icon(color=elev_color(el))))
    # add circular postion marker
    fg_vol.add_child(folium.CircleMarker(location=[lt, ln], popup=folium.Popup(iframe), radius=6, 
    fill_color=elev_color(el), color='grey', fill_opacity=0.7))

fg_pop = folium.FeatureGroup("Population")
# add country borders using GeoJson data
fg_pop.add_child(folium.GeoJson(data=open('world.json', encoding='utf-8-sig').read(), 
# color polygons based on the population
style_function=lambda x : {'fillColor':'green'} if x['properties']['POP2005'] < 10000000 
else {'fillColor' : 'orange'} if x['properties']['POP2005'] < 20000000 
else {'fillColor' : 'red'}))

# split layers into mutiple feature groups to be able to filter it using LayerControl
map1.add_child(fg_vol)
map1.add_child(fg_pop)
# adds layer control button
map1.add_child(folium.LayerControl())

map1.save('map1.html')

map2 = folium.Map(location=[lat[0], lon[0]], zoom_start=3, tiles="Mapbox Bright")
map2.save('map2.html')




