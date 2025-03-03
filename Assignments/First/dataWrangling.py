import warnings
warnings.simplefilter(action='ignore', category=FutureWarning)

import pandas as pd

file_path = ".\\tested.csv"
df = pd.read_csv(file_path)

# Display dataset info
print("Dataset Information:")
print(df.info())

# Check for missing values
print("\nMissing Values:")
print(df.isnull().sum())

# Show basic statistics
print("\nBasic Statistics:")
print(df.describe())

# Remove duplicate records
df_cleaned = df.drop_duplicates()

# Fill missing values
df_cleaned["Age"].fillna(df_cleaned["Age"].median(), inplace=True)  
df_cleaned["Fare"].fillna(df_cleaned["Fare"].median(), inplace=True)
df_cleaned["Cabin"].fillna("Unknown", inplace=True)

# Display cleaned dataset
print("\nCleaned Dataset (First 5 Rows):")
print(df_cleaned.head())

# Data Aggregation: Total Fare per Passenger Class (Pclass)
revenue_per_class = df_cleaned.groupby("Pclass")["Fare"].sum().reset_index()

print("\nTotal Fare per Passenger Class:")
print(revenue_per_class)
