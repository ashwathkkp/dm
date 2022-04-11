import csv
import pandas as pd

def import_data(file_name):
    with open(file_name,'r') as f:
        reader = csv.reader(f)
        headers = next(reader)
        data = [{h: int(x) if x.isnumeric() else x  for (h,x) in zip(headers,row)} for row in reader]
    return data

dataset = []
chicago_data = pd.DataFrame(import_data("chicago.csv"))
newyork_data = pd.DataFrame(import_data("newyork.csv"))
toronto_data = pd.DataFrame(import_data("toronto.csv"))
vancouver_data = pd.DataFrame(import_data("vancouver.csv"))

# Drill Up
#"USA": ["Chicago", "New York"],
#"Cannada": ["Toronto", "Vancouver"]

usa_data = chicago_data.add(newyork_data, fill_value=0)
print(usa_data)

cannada_data = toronto_data.add(vancouver_data, fill_value=0)
print(cannada_data)

# Roll Down
