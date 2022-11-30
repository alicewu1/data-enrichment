# data-enrichment
**HHA507 / Data Science / Assignment 3 / Data Enrichment**

## This repo aims to:
- enrich a **Hospital Inpatient Discharges 2015** (SPARCS.csv) with **Neighborhood Atlas Data-NY 2019** (e.g. zipcode, county, city, state)

## **Datasets Used:**
- [Hospital Inpatient Discharges (SPARCS) 2015 NYDOH de-identified data](https://health.data.ny.gov/Health/Hospital-Inpatient-Discharges-SPARCS-De-Identified/82xm-y6g8)
- [Neighborhood Atlas](https://www.neighborhoodatlas.medicine.wisc.edu/)
 


# Clean both sets before beginning data enrichment
- https://github.com/alicewu1/data-enrichment/blob/609c1db696d96c9b8d0f25591d656d40fe082444/scripts/enrichment.py#L4-L76


# Enrich SPARCS.csv with Neighborhood Atlas Data-NY 2019
- https://github.com/alicewu1/data-enrichment/blob/609c1db696d96c9b8d0f25591d656d40fe082444/scripts/enrichment.py#L80-L104


# Merge changes and Export the enriched dataframe as new .csv files located in: **data/enriched_SPARCS.csv**
- https://github.com/alicewu1/data-enrichment/blob/609c1db696d96c9b8d0f25591d656d40fe082444/scripts/enrichment.py#L107-L111




## Errors:
- [RESOLVED] The .csv files stored in data folder exceeded GitHub's file size and cannot be uploaded (screenshot included).
- Added the data files below to .gitignore:
  - 'neighborhood_atlas_ny_2019.csv'
  - 'SPARCS.csv'
  - 'enriched_SPARCS.csv'
