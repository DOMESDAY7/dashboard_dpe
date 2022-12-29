from Dataset import Dataset
from model_histogramme import Histogramme
from model_histogramme2 import Histogramme2

data = Dataset(select=("annee_construction", "latitude", "longitude",
               "classe_consommation_energie", "estimation_ges", "tv016_departement_code", "geo_adresse", "consommation_energie"), size=10000)

def update(year_GES=2020,year_energie=2020):

    
    histo = Histogramme(data, year=year_GES)
    histo = histo.get_histo()

    histo2=Histogramme2(data,year=year_energie)
    histo2=histo2.get_histo2()
    return histo, histo2
