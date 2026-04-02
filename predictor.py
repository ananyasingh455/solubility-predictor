import pandas as pd
import os

# Define the local filename
file_name = "dataset.csv"

# Check if the file exists in the same folder as the script
if os.path.exists(file_name):
    df = pd.read_csv(file_name)
    print(f"Successfully loaded {len(df)} molecules from local dataset.")
else:
    print(f"Error: {file_name} not found! Please download it to this folder.")
    # Fallback to URL if local file is missing
    url = "https://raw.githubusercontent.com/dataprofessor/data/master/delaney_solubility_with_descriptors.csv"
    df = pd.read_csv(url)
    print("Loaded from URL as fallback.")
    