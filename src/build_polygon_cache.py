
import time
import osmnx as ox
import geopandas as gpd
import pandas as pd

from generate_data import CITY_DISTRICTS_WEIGHTS  # dasselbe Dict, keine Kopie pflegen


def main():
    gdfs = []
    for name, (query, _) in CITY_DISTRICTS_WEIGHTS.items():
        print(f"Geocoding: {query}")
        gdf = ox.geocode_to_gdf(query)
        gdf["stadtteil"] = name
        gdfs.append(gdf[["stadtteil", "geometry"]])
        time.sleep(1)  # Nominatim-Rate-Limit: max. 1 Request/Sekunde

    combined = gpd.GeoDataFrame(pd.concat(gdfs, ignore_index=True), crs="EPSG:4326")
    combined.to_file("data/stadtteile.geojson", driver="GeoJSON")
    print(f"\n{len(combined)} Polygone geschrieben nach data/stadtteile.geojson")


if __name__ == "__main__":
    main()