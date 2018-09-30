# Pandas basics
# Developed by Wes McKinney
# Key data structure is DataFrame
# DataFrame stores and manipulates tabular data
# in rows of observations and columns of variables
# Create DataFrame with dictionary
dict = {"country": ["Brazil", "Russia", "India", "China", "South Africa"],
       "capital": ["Brasilia", "Moscow", "New Dehli", "Beijing", "Pretoria"],
       "area": [8.516, 17.10, 3.286, 9.597, 1.221],
       "population": [200.4, 143.5, 1252, 1357, 52.98] }

import pandas as pd
brics = pd.DataFrame(dict)
print(brics)

# Pandas assigns key for each country
# Use different index values
# Set the index for brics
brics.index = ["BR", "RU", "IN", "CH", "SA"]

# Print out brics with new index values
print(brics)

# Use comma separated file cars.csv

# Import the cars.csv data: cars
cars = pd.read_csv('cars.csv', index_col = 0)

# Print out cars
print(cars)

# Indexing DataFrames
# Use square bracket notation
# One column selection
# single bracket will output Pandas Series
# double bracket will output Pandas DataFrame
# Print out country column as Pandas Series
print(cars['cars_per_cap'])

# Print out country column as Pandas DataFrame
print(cars[['cars_per_cap']])

# Print out DataFrame with country and drives_right columns
print(cars[['cars_per_cap', 'country']])

# Square brackets for rows from a DataFrame
# Print out first 4 observations
print(cars[0:4])

# Print out fifth, sixth, and seventh observation
print(cars[4:6])

# Use loc and iloc to select data
# loc is label-based -> use labels
# iloc is index based -> use integer index
# Print out observation for Japan
print(cars.iloc[2])

# Print out observations for Australia and Egypt
print(cars.loc[['AUS', 'EG']])