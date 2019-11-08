###
###   Citadel Datathon 2019 Exporatory Data Analysis
###
###
###
###

# IMPORTING PACKAGES
import numpy as np
import pandas as pd

# IMPORTING DATA

house_df = pd.read_csv('House.csv') # Importing data as a dataframe

# Print the head of the dataset to give us an idea of the data

print(house_df.info())
print(house_df.head())