# house_pricing_index_united_states

**Average Housing Price Index United States 1991-2023**

**1. Use Python to extract data from the file "HPI_file.json" and convert it to an Excel file.**

```hpi_excel.py```

```python
import pandas as pd
json_file_path = r'C:\HPI_master.json'
excel_file_path = r'C:\HPI_master.xlsx'
df = pd.read_json(json_file_path)
df.to_excel(excel_file_path, index=False)
print("HPI_master.xlsx")
```

```HPI_master.xlsx```

**2. Use Python to extract data from 'HPI_file.json' and convert it to a CSV file.**

```hpi_csv.py```

```python
import pandas as pd
json_file_path = r'C:\HPI_master.json'
output_csv_file_path = r'C:\HPI_master_output.csv'
df = pd.read_json(json_file_path)
df.to_csv(output_csv_file_path, index=False)
print("HPI_master_output.csv")
```

```HPI_master_output.csv```

**3. Save the file 'HPI_master.xlsx' as 'house_pricing_index_united_states.xlsx'.**

**4. Please format the data in proper prose and put it in a table to improve readability.**

```Answer: =PROPER(A2:J124815)```

**4. What is the average for both Non-Seasonally Adjusted and Seasonally Adjusted?**

```Answer: Non-Seasonally Adjusted - NSA =AVERAGE(I2:I124815): 179,61```

```Answer: Seasonally Adjusted - SA =AVERAGE(J2:J124815): 201,37```
