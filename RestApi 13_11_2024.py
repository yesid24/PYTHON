import pandas as pd
from nba_api.stats.static import teams
import matplotlib.pyplot as plt
from nba_api.stats.endpoints import leaguegamefinder
import requests
#Yesid Cruz
def one_dict(list_dict):
    keys = list_dict[0].keys()
    out_dict = {key: [] for key in keys}
    for dict_ in list_dict:
        for key, value in dict_.items():
            out_dict[key].append(value)
    return out_dict

# Obtener la lista de equipos de la NBA
nba_teams = teams.get_teams()

# Convertir la lista de diccionarios en un DataFrame de pandas
dict_nba_team = one_dict(nba_teams)
df_teams = pd.DataFrame(dict_nba_team)

# Mostrar los primeros 3 equipos
print(df_teams.head(3))

# Filtrar el equipo de los Warriors
df_warriors = df_teams[df_teams['nickname'] == 'Warriors']
print(df_warriors)

# Obtener el ID de los Warriors
id_warriors = df_warriors[['id']].values[0][0]
print(id_warriors)

# Descargar el archivo Golden_State.pkl
filename = "https://s3-api.us-geo.objectstorage.softlayer.net/cf-courses-data/CognitiveClass/PY0101EN/Chapter%205/Labs/Golden_State.pkl"

def download(url, filename):
    response = requests.get(url)
    if response.status_code == 200:
        with open(filename, "wb") as f:
            f.write(response.content)

download(filename, "Golden_State.pkl")

# Leer el archivo descargado
file_name = "Golden_State.pkl"
games = pd.read_pickle(file_name)
print(games.head())

# Filtrar los juegos en casa y fuera de casa
games_home = games[games['MATCHUP'].str.contains('GSW vs.')]
games_away = games[games['MATCHUP'].str.contains('GSW @')]

# Calcular la media de la columna PTS para games_home y games_away
mean_pts_home = games_home['PTS'].mean()
mean_pts_away = games_away['PTS'].mean()

print(f"Media de PTS en casa: {mean_pts_home}")
print(f"Media de PTS fuera de casa: {mean_pts_away}")

# Graficar los datos
fig, ax = plt.subplots()
games_away.plot(x='GAME_DATE', y='PLUS_MINUS', ax=ax)
games_home.plot(x='GAME_DATE', y='PLUS_MINUS', ax=ax)
ax.legend(["away", "home"])
plt.show()

# Mostrar el DataFrame de equipos
print(df_teams)