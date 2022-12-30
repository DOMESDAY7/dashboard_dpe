from Dataset import Dataset
from model_histogramme_average_GES import Histogramme_average_GES
from model_histogramme_average_energie import Histogramme_average_energie

data = Dataset(select=("annee_construction",
               "estimation_ges", "geo_adresse", "consommation_energie"), size=10000)

def update( begin_year_GES=1950,end_year_GES=2020,begin_year_energie=1950,end_year_energie=2020):

    
    histo = Histogramme_average_GES(data, begin_year=begin_year_GES, end_year=end_year_GES)
    histo = histo.get_histo()

    histo2=Histogramme_average_energie(data, begin_year=begin_year_energie, end_year=end_year_energie)
    histo2=histo2.get_histo2()
    return histo, histo2
