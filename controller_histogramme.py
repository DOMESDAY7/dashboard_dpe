from Dataset import Dataset
from model_histogramme import Histogramme

def update(year=2020):
    data = Dataset(select=("annee_construction", "latitude", "longitude",
               "classe_estimation_ges", "estimation_ges", "tv016_departement_code", "geo_adresse"), size=10000)

    histo = Histogramme(data, year=year)
    histo = histo.get_histo()
    return histo
