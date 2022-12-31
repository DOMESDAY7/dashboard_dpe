import pandas as pd
from Dataset import Dataset
from model_dpe_map import DpeMap

data = Dataset(select=("annee_construction", "latitude", "longitude",
               "classe_estimation_ges", "estimation_ges", "tv016_departement_code", "geo_adresse"), size=10000)

# convert the data to a dataframe
data = pd.DataFrame(data.get_data()["results"])

# rename the column to be more readable
data.rename(
    columns={"classe_estimation_ges": "Classe consommation d'énergie"}, inplace=True)
data.rename(columns={"geo_adresse": "Adresse"}, inplace=True)

# sort the dataframe by the column "Classe consommation d'énergie"
data.sort_values(by=["Classe consommation d'énergie"], inplace=True)

# convert the dataframe to a DpeMap object
figMap = DpeMap(data)
figMap = figMap.get_map()
