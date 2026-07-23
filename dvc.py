import pandas as pd
import os

# Create a sample DataFrame with column names
data = {'Name': ['Alice', 'Bob', 'Charlie'],
      'Age': [25, 30, 35],
      'City': ['New York', 'Los Angeles', 'Chicago']
    }

df = pd.DataFrame(data)
new_row_loc = {'Name': 'V2', 'Age': 20, 'City': 'City1'}
df.loc[len(df.index)] = new_row_loc
new_row_loc2 = {'Name': 'V3', 'Age': 30, 'City': 'City1'}
df.loc[len(df.index)] = new_row_loc2
data_dir='data'
os.makedirs(data_dir,exist_ok=True)
 
file_path=os.path.join(data_dir,'simple_data.csv')

df.to_csv(file_path,index=False)

print(f"csv file saved to {file_path}")
