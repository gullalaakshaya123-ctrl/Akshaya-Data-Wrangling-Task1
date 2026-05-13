import pandas as pd
import numpy as np

# Load dataset
file_path = "housing_data.csv"
df = pd.read_csv(file_path)

print("Dataset Loaded Successfully!")
print("Original Dataset Shape:", df.shape)
print("\nFirst 5 Rows:\n", df.head())
print("\nMissing Values Before Cleaning:\n", df.isnull().sum())
print("\nDuplicate Rows:", df.duplicated().sum())

# Remove duplicates
df.drop_duplicates(inplace=True)

# Standardize column names FIRST
df.columns = df.columns.str.strip().str.lower().str.replace(' ', '_')

# Fill missing numerical values
numerical_cols = df.select_dtypes(include=[np.number]).columns
for col in numerical_cols:
    df[col] = df[col].fillna(df[col].median())

# Fill missing categorical values
categorical_cols = df.select_dtypes(include=['object', 'string']).columns
for col in categorical_cols:
    df[col] = df[col].fillna(df[col].mode()[0])

# Handle outliers using IQR
for col in numerical_cols:
    Q1 = df[col].quantile(0.25)
    Q3 = df[col].quantile(0.75)
    IQR = Q3 - Q1

    lower_bound = Q1 - 1.5 * IQR
    upper_bound = Q3 + 1.5 * IQR

    df[col] = np.where(df[col] < lower_bound, lower_bound, df[col])
    df[col] = np.where(df[col] > upper_bound, upper_bound, df[col])

# Feature engineering
if 'year_built' in df.columns:
    current_year = 2026
    df['house_age'] = current_year - df['year_built']

# Save cleaned dataset
output_file = "cleaned_housing_data.csv"
df.to_csv(output_file, index=False)

print("\nCleaned Dataset Shape:", df.shape)
print("\nMissing Values After Cleaning:\n", df.isnull().sum())
print("\nData cleaning completed successfully!")
print(f"\nCleaned file saved as: {output_file}")