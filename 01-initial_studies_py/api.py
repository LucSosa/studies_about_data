# %%
import requests
import pandas as pd

url = "https://api.opendota.com/api/heroes"
response = requests.get(url)

# %%
response.status_code
data = response.json()

for i in data:
    print(i['localized_name'])

# %%
df = pd.DataFrame(data)
df.to_csv("heroes_dota.csv", sep=";")

# %%
url = "https://api.opendota.com/api/proMatches"
data = requests.get(url).json()
df_partida = pd.DataFrame(data)
df_partida.to_csv("partidas_dota.csv", sep=";")

# %%
df_partida
