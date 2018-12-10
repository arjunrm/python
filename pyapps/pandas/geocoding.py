import pandas
from geopy.geocoders import ArcGIS

arc_gis = ArcGIS()

# geo_coord = arc_gis.geocode("3995 23rd st, San Francisco, CA 94114")
# print(geo_coord.address)
# print(geo_coord.latitude, geo_coord.longitude, geo_coord.altitude)

# geo_coord = arc_gis.geocode("Robert Bosch, Hildesheim")
# print(geo_coord.address)
# print(geo_coord.latitude, geo_coord.longitude, geo_coord.altitude)

# geo_coord = arc_gis.geocode("Robert Bosch, Hosur Road, Bangalore")
# print(geo_coord.address)
# print(geo_coord.latitude, geo_coord.longitude, geo_coord.altitude)

def get_lat_lon(address):
    arc_gis = ArcGIS()
    geo_code = arc_gis.geocode(address)
    return str(geo_code.latitude) + "," + str(geo_code.longitude)

df = pandas.read_excel('supermarkets.xlsx')
df["Address"] = df["Address"] + "," + df["City"] + "," + df["State"] + "," + df["Country"]
print(df["Address"])

df["LatLong"] = df["Address"].apply(get_lat_lon)
print(df["LatLong"])

df["Coordinates"] = df["Address"].apply(arc_gis.geocode)
print(df["Coordinates"])

df["Latitude"] = df["Coordinates"].apply(lambda x : x.latitude)
print(df["Latitude"])


