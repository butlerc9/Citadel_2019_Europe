###
###   Citadel Datathon 2019 Exporatory Data Analysis
###
###   Team:
###   Cormac Butler    Ronan Prendiville
###   Nicholas Kim     Jonas Walheim
###

# IMPORTING PACKAGES
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# IMPORTING DATA
#%%
house_df = pd.read_csv('House.csv') # Importing data as a dataframe

#print(house_df.loc[1]) # get first data point
#print(house_df['Size']) # get first data set


# BASIC INFORMATION
#%%
print(house_df.info()) #gives info on the data set, all should be same length
print(house_df.head())
print(house_df.shape)
print(house_df.columns)

# CHECK FOR MISSING AND NULL VALUES
#%%
print(house_df.isnull().sum())
print(house_df.isna().sum())

#house_df.dropna() #removes all rows with NA values
#house_df.dropna(axis=1) # removes all columns with NA values

print("\n \n Summary of lot statistic") #run a summary on one particular variable
print( house_df['Price '].describe())


# Selecting Results with a Particular Criterea
#%%

house_df[house_df['Lot ']==4] # Here we are selecting all of the 
                              # houses with a lot value of 4

house_df[house_df['Year'] > 1990].head(3) # Get all years greater than 1990

# CREATE A FUNCTION TO ITERATTE OVER
#%%

# have created a function where when we apply a function
# it will categorize it as expensive or cheap
def expense_function(x):
    if x > house_df['Price '].median():
        return "expensive"
    else:
        return "affordable"

# apply it individually to each of the data pieces
house_df["Price Category"] = house_df['Price '].apply(expense_function)

#%%
plt.show(house_df.corr())
