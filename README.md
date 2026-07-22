# Johnson & Johnson - Deutschlandticket Adoption Analysis

This repository contains pipeline for estimating the Deutschlandticket adoption potential among Johnson & Johnson employees at the Norderstedt office using synthetic data. 

To ensure clean code and separation of concerns, the project is split into raw data generation and the final business analysis notebook.

## Repository Structure
* `src/generate_data.py`: Generates 2,000 synthetic employee locations weighted by real Hamburg district population densities and assigns car-ownership proxies.
* `src/compute_routes.py`: Utilizes `r5py` and open GTFS/OSM data to calculate door-to-door public transport commute times.
* `J&J_Deutschlandticket_Analysis.ipynb`: A Jupyter Notebook containing the business logic and adoption heuristics.
* `data/`: Contains the generated CSV datasets and the interactive standalone map (`map.html`) aswell as the (`check_polygons.html`) wich was generated to ensure that the polygons used were correct.


## Prerequisites

To run the routing engine (`r5py`) locally, the following system requirements must be met:
* **Python:** Version 3.9 or higher.
* **Java:** Java Development Kit (JDK) 21 or higher. 

## Key Findings

Based on the synthetic number of 2,000 employees, the analysis reveals the following key insights:
* **Commute Viability:** Approximately **3%** of the workforce resides within a highly viable public transit commute of under 45 minutes to the Norderstedt office.
* **Adoption Potential:** Factoring in commute times and car ownership as a convenience proxy, the estimated overall adoption rate for the Deutschlandticket sits at **5.4%**.


## Assumptions & Limitations

To deliver a robust, reproducible prototype within the time constraints of this assessment, several analytical boundaries were set:

* **Synthetic Data:** No real employee data was utilized. Locations were generated via random spatial sampling, weighted by actual district population densities.

* **Spatial Outliers (Synthetic Data Artifacts):** Because employee coordinates were generated randomly within district polygons, some points fall onto unroutable terrain (e.g., lakes, fenced industrial zones, or dense forests) lacking pedestrian infrastructure in OpenStreetMap. The routing engine correctly identifies these as inaccessible, which explains why a few synthetic employees appear as red points on the map despite their geographical proximity to the office.

* **Scoring:** The adoption weights (e.g., 90% likelihood for <30 mins) and the 25% car ownership penalty are estimates. In a production setting, these would be calculated using historical HR commuter data.

* **Static Transit Routing:** The model evaluates a fixed morning arrival time.

* **Proxy Variables:** Instead of a routing engine for car commute times, car ownership was used  to model convenience.

* **Remote Workers:** Remote/hybrid employees are not taken into account. (since they have less days in the office the adoption rate would be lower for them).
