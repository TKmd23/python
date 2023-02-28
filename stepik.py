import pandas as pd
import json

with open('cd_ua_2023-01-json') as f:
    data = json.load(f)

df = pd.DataFrame.from_dict(data)


df.to_excel('file.xlsx', index=False)

