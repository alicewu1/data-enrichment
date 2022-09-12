# data-enrichment
**For HHA507 Assignment 3**

This repo aims to enrich a Hospital Inpatient Discharges (SPARCS) 2015 csv with Neighborhood Atlas Data for NY in 2019.

1. I cleaned the 2 datasets before beginning data enrichment
2. I enriched SPARCS.csv with Neighborhood Atlas NY 2019 Data (zipcode, county, city, state)
3. I exported the dataframe into a new .csv filed located in data/enriched_SPARCS.csv

**Datasets Used:**
1. Neighborhood Atlas: https://www.neighborhoodatlas.medicine.wisc.edu/ 
2. Hospital Inpatient Discharges (SPARCS) 2015 NYDOH de-identified data (.csv): https://health.data.ny.gov/Health/Hospital-Inpatient-Discharges-SPARCS-De-Identified/82xm-y6g8  


**Errors:**
The .csv files stored in data folder exceeded GitHub's file size and cannot be uploaded (screenshot included).
Data files added to .gitignore file:

1. 'neighborhood_atlas_ny_2019.csv'
2. 'SPARCS.csv'
3. 'enriched_SPARCS.csv'