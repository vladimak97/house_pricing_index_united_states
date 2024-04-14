import pandas as pd

# File paths for input JSON and output CSV files
json_file_path = r'C:\HPI_master.json'

output_csv_file_path = r'C:\HPI_master_output.csv'

# Reading JSON data
df = pd.read_json(json_file_path)

# Saving DataFrame to CSV
df.to_csv(output_csv_file_path, index=False)

# Indicating successful completion
print("HPI_master_output.csv")
