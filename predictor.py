import pandas as pd
import os
import matplotlib.pyplot as plt

# File name
file_name = "dataset.csv"

# Step 1: Load dataset
if os.path.exists(file_name):
    df = pd.read_csv(file_name)
    print(f"Successfully loaded {len(df)} molecules from local dataset.")
else:
    print(f"{file_name} not found. Loading from URL...")
    url = "https://raw.githubusercontent.com/dataprofessor/data/master/delaney_solubility_with_descriptors.csv"
    df = pd.read_csv(url)
    print("Loaded dataset from URL.")
    
    # Save locally for future use
    df.to_csv(file_name, index=False)
    print("Dataset saved locally.")

# Step 2: Preview data
print("\nFirst 5 rows:")
print(df.head())

# Step 3: Dataset info
print("\nDataset Info:")
print(df.info())

# Step 4: Basic statistics
print("\nStatistical Summary:")
print(df.describe())

# Step 5: Plot LogS distribution
if 'LogS' in df.columns:
    plt.figure()
    plt.hist(df['LogS'], bins=10)
    plt.xlabel("LogS (Solubility)")
    plt.ylabel("Frequency")
    plt.title("Distribution of Solubility")
    plt.show()
else:
    print("Column 'LogS' not found in dataset.")