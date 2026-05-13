import pandas as pd
import numpy as np

# Create sample housing dataset
data = {
    'Price': [500000, 650000, 700000, np.nan, 850000, 600000, 750000, 900000, 620000, 580000],
    'Area': [1500, 1800, 2000, 1700, np.nan, 1600, 2100, 2500, 1750, 1550],
    'Bedrooms': [3, 4, 4, 3, 5, np.nan, 4, 5, 3, 3],
    'Bathrooms': [2, 3, 3, 2, 4, 2, 3, np.nan, 2, 2],
    'Stories': [1, 2, 2, 1, 3, 2, 2, 3, 1, 1],
    'Parking': [1, 2, 2, 1, 3, 2, np.nan, 3, 1, 1],
    'FurnishingStatus': [
        'Furnished', 'Semi-Furnished', 'Unfurnished', np.nan, 'Furnished',
        'Semi-Furnished', 'Furnished', 'Unfurnished', 'Semi-Furnished', 'Furnished'
    ],
    'Year Built': [2010, 2015, 2018, 2012, 2020, 2014, 2017, 2021, 2011, 2013]
}

# Convert to DataFrame
df = pd.DataFrame(data)

# Add duplicate row intentionally
df = pd.concat([df, df.iloc[[2]]], ignore_index=True)

# Save dataset
df.to_csv("housing_data.csv", index=False)

print("housing_data.csv created successfully!")