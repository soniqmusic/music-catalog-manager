import pandas as pd
import os

# Define the data directory
data_dir = 'app/data'

# List all files in the data directory
files = os.listdir(data_dir)

# Process each file
for file in files:
    file_path = os.path.join(data_dir, file)
    if file.endswith('.xlsx'):
        # Read Excel file
        df = pd.read_excel(file_path)
        print(f"Processed {file}:\n", df.head())
    elif file.endswith('.csv'):
        # Read CSV file
        df = pd.read_csv(file_path)
        print(f"Processed {file}:\n", df.head())