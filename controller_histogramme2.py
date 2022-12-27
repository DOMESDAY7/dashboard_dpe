from model_histogramme2 import Histogramme2
from Dataset import Dataset

data = Dataset(select=("annee_construction", "latitude", "longitude",
               "classe_estimation_ges", "estimation_ges", "tv016_departement_code", "geo_adresse"), size=10000)

histo2=Histogramme2(data)
histo2=histo2.get_histo2()