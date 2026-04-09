 import pandas as pd
import os
import matplotlib.pyplot as plt

file_name = "dataset.csv"

if os.path.exists(file_name):
    df = pd.read_csv(file_name)
    print(f" Successfully loaded {len(df)} molecules from local dataset.")
else:
    print(f" {file_name} not found. Loading from URL...")
    url = "https://raw.githubusercontent.com/dataprofessor/data/master/delaney_solubility_with_descriptors.csv"
    df = pd.read_csv(url)
    print(" Loaded dataset from URL.")


print("\nDataset Preview:")
print(df)
    
compound_name = input("\nEnter the Compound ID to visualize: ").strip()

molecule = df[df['Compound ID'].str.lower() == compound_name.lower()]

if not molecule.empty:
    logs_value = molecule['LogS'].values[0]
    
    plt.figure(figsize=(10, 6))
    
    df['LogS'].plot( kind='hist', bins=20, density=True, alpha=0.6, edgecolor='black', label='Dataset Distribution' )
    
    df['LogS'].plot( kind='density', linewidth=2, label='Density Curve' )
    
    plt.axvline( logs_value,  color='red', linestyle='solid', linewidth=2, label=f'{compound_name} (LogS = {logs_value})' )
    
    plt.title("Solubility Distribution with Selected Molecule")
    plt.xlabel("LogS")
    plt.ylabel("Density")
    plt.legend()
    plt.grid(True, linestyle='--', alpha=0.6)
    plt.tight_layout()
    plt.show()
    
    print(f"\n {compound_name} LogS Value: {logs_value}")
else:
    print(" Molecule not found in the dataset.")

     
    df.to_csv(file_name, index=False)
    print(" Dataset saved locally as 'dataset.csv'.") 

print("\n Statistical Summary:")
print(df.describe())

if 'LogS' in df.columns:
    plt.figure(figsize=(10, 6))
    
    df['LogS'].plot( kind='hist', bins=20,  density=True, alpha=0.6, edgecolor='black', label='Histogram')

    df['LogS'].plot( kind='density', linewidth=2, label='Density Curve')
 
    mean_value = df['LogS'].mean()
    median_value = df['LogS'].median()

    plt.axvline(mean_value, linestyle='dashed', linewidth=2,
                label=f'Mean: {mean_value:.2f}')
    plt.axvline(median_value, linestyle='dotted', linewidth=2,
                label=f'Median: {median_value:.2f}')

    plt.title("Histogram and Density Plot of LogS (Solubility)", fontsize=14, fontweight='bold')
    plt.xlabel("LogS (Solubility)", fontsize=12)
    plt.ylabel("Density", fontsize=12)
    plt.grid(True, linestyle='--', alpha=0.6)
    plt.legend()
    plt.tight_layout()

else:
    print(" Column 'LogS' not found in dataset.")
