import pandas as pd

# File paths for input and output
json_file_path = r'C:\HPI_master.json'

excel_file_path = r'C:\HPI_master.xlsx'

# Reading JSON data
df = pd.read_json(json_file_path)

# Saving DataFrame to Excel
df.to_excel(excel_file_path, index=False)

# Indicating successful completion
print("HPI_master.xlsx")