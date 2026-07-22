
import datetime
import pandas as pd
import geopandas as gpd
from shapely.geometry import Point
from r5py import TransportNetwork, TravelTimeMatrix, TransportMode
 

JJ_LAT, JJ_LON = 53.6866, 9.9934
OSM_PATH        = "data/hamburg-latest.osm.pbf"
GTFS_PATH       = "data/GTFS.zip"
EMPLOYEES_PATH  = "data/employees.csv"
OUTPUT_PATH     = "data/commute_results.csv"
 
DEPARTURE = datetime.datetime(2026, 7, 23, 8, 0)
 
 
# loading employees.csv as gdf
def load_origins(path):
 
    df = pd.read_csv(path)
    df = df.rename(columns={"employee_id": "id"})
    gdf = gpd.GeoDataFrame(
        df,
        geometry=gpd.points_from_xy(df["lon"], df["lat"]),
        crs="EPSG:4326"  #coordinates are longitude and latitude (theformat that is needed)
    )
    return gdf
 
 #could have been hardcoded for this assignment
def build_destination():
    return gpd.GeoDataFrame(
        {"id": ["JJ_Office"]},
        geometry=[Point(JJ_LON, JJ_LAT)],
        crs="EPSG:4326"
    )
 
 

def main():
    origins     = load_origins(EMPLOYEES_PATH)
    destination = build_destination()
 
   
    network = TransportNetwork(OSM_PATH, [GTFS_PATH])
 
    matrix = TravelTimeMatrix(
        network,
        origins=origins,
        destinations=destination,
        departure=DEPARTURE,
        transport_modes=[TransportMode.TRANSIT, TransportMode.WALK]
    )
 

    result = matrix.rename(columns={
        "from_id":     "employee_id",
        "travel_time": "travel_time_min"
    })
    result = result[["employee_id", "travel_time_min"]]
 
    # NaN-Check
    n_nan = result["travel_time_min"].isna().sum()
    if n_nan > 0:
        print(f"{n_nan} Employees without Routing-Result (NaN).")
 
    result.to_csv(OUTPUT_PATH, index=False)
    print(f"\nsaved at: {OUTPUT_PATH}")
    print(result["travel_time_min"].describe().round(1))
 
 
if __name__ == "__main__":
    main()