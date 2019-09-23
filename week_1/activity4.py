import requests
import pandas as pd
url = 'https://data.cityofnewyork.us/api/views/kku6-nxdu/rows.json'

resp = requests.get(url=url)
data = resp.json()


json_data = data['data']
print(json_data)
columns = []
for c in data['meta']['view']['columns']:
    columns.append(c['name'])

df = pd.DataFrame(data=json_data, columns=columns)


# View the first ten rows
print(df.head(10))
