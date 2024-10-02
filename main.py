import yaml
import pandas as pd

with open('data/1970/races/02-monaco/race-results.yml', 'r') as file:
    yml_data = yaml.safe_load(file)

df = pd.DataFrame(yml_data)

print(df)