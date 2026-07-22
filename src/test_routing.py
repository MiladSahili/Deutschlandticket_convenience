
import datetime
import geopandas as gpd
from shapely.geometry import Point


from r5py import TransportNetwork, TravelTimeMatrix, TransportMode

transport_network = TransportNetwork(
    "data/hamburg-latest.osm.pbf",
    ["data/GTFS.zip"]
)

# example point in Eimsbüttel
origins = gpd.GeoDataFrame(
    {"id": ["Eimsbuettel_01"]},  
    geometry=[Point(9.97, 53.57)],  
    crs="EPSG:4326"
)

destinations = gpd.GeoDataFrame(
    {"id": ["JJ_Office"]},     
    geometry=[Point(9.9934, 53.6866)],  
    crs="EPSG:4326"
)


matrix = TravelTimeMatrix(
    transport_network,
    origins=origins,
    destinations=destinations,
    departure=datetime.datetime(2026, 7, 23, 8, 0), 
    transport_modes=[TransportMode.TRANSIT, TransportMode.WALK]
)


print(matrix)