import pandas as pd
import os

# Create a sample DataFrame with column names
data = {'Name': ['Alice', 'Bob', 'Charlie'],
      'Age': [25, 30, 35],
      'City': ['New York', 'Los Angeles', 'Chicago']
    }

df = pd.DataFrame(data)

data_dir='data'
os.makedirs(data_dir,exist_ok=False)
 
file_path=os.path.join(data_dir,'simple_data.csv')

df.to_csv(file_path,index=False)

print(f"csv file saved to {file_path}")
