
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

    # Eimsbüttel (Bezirk)
    "Niendorf":         ("Niendorf, Eimsbüttel, Hamburg, Germany", 42496),
    "Schnelsen":        ("Schnelsen, Hamburg, Germany", 31323),
    "Eidelstedt":       ("Eidelstedt, Hamburg, Germany", 36705),
    "Lokstedt":         ("Lokstedt, Hamburg, Germany", 31666),
    "Stellingen":       ("Stellingen, Hamburg, Germany", 28812),
    "Eimsbüttel":       ("Eimsbüttel, Hamburg, Germany", 57798),

    # Altona (Bezirk)
    "Altona-Altstadt":  ("Altona-Altstadt, Hamburg, Germany", 29680),
    "Altona-Nord":      ("Altona-Nord, Hamburg, Germany", 26777),
    "Ottensen":         ("Ottensen, Hamburg, Germany", 35925),
    "Bahrenfeld":       ("Bahrenfeld, Hamburg, Germany", 31051),
    "Lurup":            ("Lurup, Hamburg, Germany", 37755),
    "Osdorf":           ("Osdorf, Hamburg, Germany", 26601),

    # Hamburg-Mitte
    "St. Pauli":        ("St. Pauli, Hamburg, Germany", 22377),

    # Wandsbek (Bezirk)
    "Bramfeld":         ("Bramfeld, Hamburg, Germany", 53543),
    "Poppenbüttel":     ("Poppenbüttel, Hamburg, Germany", 24598),
    "Hummelsbüttel":    ("Hummelsbüttel, Hamburg, Germany", 18731),
    "Wandsbek":         ("Wandsbek, Hamburg, Germany", 38397),
    "Rahlstedt":        ("Rahlstedt, Hamburg, Germany", 95836),
    "Farmsen-Berne":    ("Farmsen-Berne, Hamburg, Germany", 39266),

    # Schleswig-Holstein (Näherungswerte, kein zentrales Melderegister)
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

    # Eimsbüttel (Ergänzung)
    "Hoheluft-West":    ("Hoheluft-West, Hamburg, Germany", 13641),

    # Wandsbek (Ergänzung)
    "Steilshoop":       ("Steilshoop, Hamburg, Germany", 19902),
}

