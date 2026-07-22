import numpy as np         
import pandas as pd         
import geopandas as gpd    
from shapely.geometry import Point   


SEED = 89
N_EMPLOYEES = 2000


JJ_LAT , JJ_LON = 53.6866, 9.9934   # Robert-Koch-Straße 1, Norderstedtja

#The weights are the amount of citizens in that district
CITY_DISTRICTS_WEIGHTS = {
    # name: (nominatim_query, einwohner)
    # Hamburg-Nord
    "Langenhorn":       ("Langenhorn, Hamburg, Germany", 48901),
    "Fuhlsbüttel":      ("Fuhlsbüttel, Hamburg, Germany", 13984),
    "Ohlsdorf":         ("Ohlsdorf, Hamburg, Germany", 17813),
    "Alsterdorf":       ("Alsterdorf, Hamburg, Germany", 15644),
    "Groß Borstel":     ("Groß Borstel, Hamburg, Germany", 10939),
    "Winterhude":       ("Winterhude, Hamburg, Germany", 61192),
    "Barmbek-Nord":     ("Barmbek-Nord, Hamburg, Germany", 44062),
    "Barmbek-Süd":      ("Barmbek-Süd, Hamburg, Germany", 37091),
    "Eppendorf":        ("Eppendorf, Hamburg, Germany", 25234),

    # Eimsbüttel 
    "Niendorf":         ("Niendorf, Eimsbüttel, Hamburg, Germany", 42496),
    "Schnelsen":        ("Schnelsen, Hamburg, Germany", 31323),
    "Eidelstedt":       ("Eidelstedt, Hamburg, Germany", 36705),
    "Lokstedt":         ("Lokstedt, Hamburg, Germany", 31666),
    "Stellingen":       ("Stellingen, Hamburg, Germany", 28812),
    "Eimsbüttel":       ("Eimsbüttel, Hamburg, Germany", 57798),

    # Altona 
    "Altona-Altstadt":  ("Altona-Altstadt, Hamburg, Germany", 29680),
    "Altona-Nord":      ("Altona-Nord, Hamburg, Germany", 26777),
    "Ottensen":         ("Ottensen, Hamburg, Germany", 35925),
    "Bahrenfeld":       ("Bahrenfeld, Hamburg, Germany", 31051),
    "Lurup":            ("Lurup, Hamburg, Germany", 37755),
    "Osdorf":           ("Osdorf, Hamburg, Germany", 26601),

    # Hamburg-Mitte
    "St. Pauli":        ("St. Pauli, Hamburg, Germany", 22377),

    # Wandsbek 
    "Bramfeld":         ("Bramfeld, Hamburg, Germany", 53543),
    "Poppenbüttel":     ("Poppenbüttel, Hamburg, Germany", 24598),
    "Hummelsbüttel":    ("Hummelsbüttel, Hamburg, Germany", 18731),
    "Wandsbek":         ("Wandsbek, Hamburg, Germany", 38397),
    "Rahlstedt":        ("Rahlstedt, Hamburg, Germany", 95836),
    "Farmsen-Berne":    ("Farmsen-Berne, Hamburg, Germany", 39266),

    # Schleswig-Holstein (roundabout citizens)
    "Norderstedt":      ("Norderstedt, Germany", 83000),
    "Henstedt-Ulzburg": ("Henstedt-Ulzburg, Germany", 28000),
    "Quickborn":        ("Quickborn, Kreis Pinneberg, Germany", 22000),
    "Kaltenkirchen":    ("Kaltenkirchen, Germany", 22000),
    "Pinneberg":        ("Pinneberg, Germany", 44000),
    "Ahrensburg":       ("Ahrensburg, Germany", 35000),
    "Elmshorn":         ("Elmshorn, Germany", 51000),
    "Bad Oldesloe":     ("Bad Oldesloe, Germany", 26000),
    "Hoheluft-Ost":     ("Hoheluft-Ost, Hamburg, Germany", 9853),
    "Dulsberg":         ("Dulsberg, Hamburg, Germany", 17230),

    # Eimsbüttel 
    "Hoheluft-West":    ("Hoheluft-West, Hamburg, Germany", 13641),

    # Wandsbek 
    "Steilshoop":       ("Steilshoop, Hamburg, Germany", 19902),
}



#assigning a district to each employee weighted with the amount of citizens of that district

def assign_district(n , rng):
    names = list(CITY_DISTRICTS_WEIGHTS.keys())
    weights = np.array([v[1] for v in CITY_DISTRICTS_WEIGHTS.values()], dtype=float)
    return rng.choice(names, size=n, p=weights / weights.sum())
       


def sample_points_in_polygon(polygon, n , rng):
    #the lon and lat from the districts
    minx, miny, maxx, maxy = polygon.bounds 
    Result = []

    while len(Result)< n:
        random_point_x = rng.uniform(minx , maxx)
        random_point_y = rng.uniform(miny, maxy)
        random_point = Point(random_point_x,random_point_y)
        if polygon.contains(random_point):
            Result.append(random_point)
    return(Result)        


def main():
    rng = np.random.default_rng(SEED)
    polygons = gpd.read_file("data/stadtteile.geojson").set_index("stadtteil")

    df = pd.DataFrame({"stadtteil": assign_district(N_EMPLOYEES, rng)})

    lat = np.empty(N_EMPLOYEES)   
    lon = np.empty(N_EMPLOYEES)

    for name, group in df.groupby("stadtteil"):  #filling the empty arrays with the real points
        pts = sample_points_in_polygon(polygons.loc[name, "geometry"], len(group), rng)
        lat[group.index] = [p.y for p in pts]
        lon[group.index] = [p.x for p in pts]

    df["lat"] = lat   
    df["lon"] = lon
  

    df.insert(0, "employee_id", [f"EMP{i:04d}" for i in range(1, N_EMPLOYEES + 1)])
 
    df["hat_auto"] = rng.random(N_EMPLOYEES) < 0.75
 

    df.to_csv("data/employees.csv", index=False)
    print(df["stadtteil"].value_counts().to_string())
    print(f"\n{len(df)} Mitarbeiter angelegt in data/employees.csv")
 
 
if __name__ == "__main__":
    main()