import json
import sys
import geojson
import shapely.wkt
from shapely.geometry import shape


with open(sys.argv[1]) as map:
    g1 = geojson.load(map)

g1 = g1["features"][0]["geometry"]
geom = shape(g1)
geomWkt = geom.wkt
print(geomWkt)
