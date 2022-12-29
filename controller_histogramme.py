from Dataset import Dataset
from model_histogramme import Histogramme
from model_histogramme2 import Histogramme2

data = Dataset(select=("annee_construction", "latitude", "longitude",
               "classe_consommation_energie", "estimation_ges", "tv016_departement_code", "geo_adresse"), size=10000)

def update(year=2020):

    
    histo = Histogramme(data, year=year)
    histo = histo.get_histo()

    histo2=Histogramme2(data)
    histo2=histo2.get_histo2()
    return histo, histo2
