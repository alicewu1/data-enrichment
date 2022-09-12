c## python -m venv . (to create venv in current directory) 
## fixed my python compatibility error

import pandas as pd
import numpy as np

### LOADING IN DATA ###
neighborhood = pd.read_csv(r"data\neighborhood_atlas_ny_2019.csv")
neighborhood # view output
sparcs = pd.read_csv("data\SPARCS.csv")
sparcs # view output 

## VIEWING COLUMN NAMES ###
neighborhood.columns
sparcs.columns

### FIRST: CLEANING DATA BEFORE DATA ENRICHMENT ####
neighborhood.columns = neighborhood.columns.str.replace('[^A-Za-z0-9]+', '_') ## regex formatting for strings
list(neighborhood)
# replace all whitespace in column names with an underscore
neighborhood.columns = neighborhood.columns.str.replace(' ', '_')
neighborhood.columns # view output

sparcs.columns = neighborhood.columns.str.replace('[A-Za-z0-9]+', '_')
list(sparcs)
sparcs.columns = sparcs.columns.str.replace(' ', '_')
sparcs # view output


## VIEWING COLUMN TYPES 
neighborhood.dtypes
sparcs.dtypes

## CONVERTING COLUMNS

# create a list of columns that are strings, and save as strings 
strings = neighborhood.select_dtypes(include=['object']).columns
# create a list of columns that are numbers, and save as numbers
numbers = neighborhood.select_dtypes(include=['int64','float64']).columns
# create a list of columns that are dates, and save as dates
dates = neighborhood.select_dtypes(include=['datetime64[ns]']).columns
# create a list of columns that are booleans, and save as booleans
booleans = neighborhood.select_dtypes(include=['bool']).columns
# create a list of columns that are objects, and save as objects
objects = neighborhood.select_dtypes(include=['object']).columns

# create a list of columns that are strings, and save as strings 
strings = sparcs.select_dtypes(include=['object']).columns
# create a list of columns that are numbers, and save as numbers
numbers = sparcs.select_dtypes(include=['int64','float64']).columns
# create a list of columns that are dates, and save as dates
dates = sparcs.select_dtypes(include=['datetime64[ns]']).columns
# create a list of columns that are booleans, and save as booleans
booleans = sparcs.select_dtypes(include=['bool']).columns
# create a list of columns that are objects, and save as objects
objects = sparcs.select_dtypes(include=['object']).columns


## LOOK FOR DUPLICATE ROWS
neighborhood.columns.duplicated()
sparcs.columns.duplicated()


## REMOVING WHITESPACE
# .sum to get a count of missing values in each column
neighborhood.isnull().sum() ## 
sparcs.isnull().sum() ## 
# replacing blank, empty cells with NaN 
#NaN tells python that it is a missing value instead of white space that we can't see
neighborhood.replace(to_replace='', value=np.nan, inplace=True) ## need to import numpy for NaaN
sparcs.replace(to_replace='', value=np.nan, inplace=True) ## need to import numpy for NaaN
# drop rows with missing values
neighborhood.dropna(inplace=True) # drop rows with missing values
neighborhood.isnull().sum() #run again to double verify whitespace was removed
sparcs.dropna(inplace=True) # drop rows with missing values
sparcs.isnull().sum() #run again to double verify whitespace was removed



### DATA ENRICHMENT ###
## enrich SPARCS csv with neighborhood atlas information by
# adding key columns from neighborhood atlas csv into SPARCS.csv
neighborhood_small = neighborhood[['ZIPID', 'ADI_NATRANK', 'ADI_STATERNK']] 
sparcs_small = sparcs [[
    'Health_Service_Area',
    'Hospital_County',
    'Facility_Name',
    'Age_Group',
    'Zip_Code_-_3_digits',
    'Gender',
    'Race',
    'Ethnicity',
    'CCS_Procedure_Code',
    'APR_DRG_Code',
    'APR_MDC_Code',
    'APR_Severity_of_Illness_Code',
    'Payment_Typology_1',
    'Total_Charges',
    'Total_Costs']]

print(neighborhood_small.sample(10).to_markdown())
neighborhood_small.shape 
print(sparcs_small.sample(10).to_markdown())
sparcs_small.shape


## MERGE CHANGES ##
enriched_SPARCS = neighborhood_small.merge(sparcs_small, how='left', left_on='ZIPID', right_on='Health_Service_Area')

## Export DataFrame into new .csv file 
enriched_SPARCS.to_csv('data/enriched_SPARCS.csv')