import pandas as pd
import os


## Creating a sample DataFrame with column names
data = {'Name':['Jason', 'Amanda', 'Charles'],
        'Age': [21, 24, 19],
        'City': ['Chicago', 'London', 'Califormia']
        }

df =pd.DataFrame(data)

## Adding a new row df for V2
new_row = {'Name': 'Gerald', 'Age': 23, 'City': 'City1'}
df.loc[len(df.index)] = new_row



## Ensuring that the "data" directory exists at the root level
data_dir = 'data'
os.makedirs(data_dir, exist_ok=True)

## Defining file path
file_path = os.path.join(data_dir, 'sample_data.csv')

## Saving the DataFrame to a CSV file, including column names
df.to_csv(file_path, index=False)

print(f"CSV file saved to {file_path}")
