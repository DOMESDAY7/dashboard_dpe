import plotly.express as px
from Dataset import Dataset
from collections import namedtuple


# t = Dataset(select=("annee_construction", "tv016_departement_code",
#             "classe_estimation_ges", "estimation_ges"), size=10000)

class Histogramme_average_energie:
    """
    To create an histogramme on an average of the energy consumption by year
    """
    def __init__(self,df, begin_year=1950, end_year=2020):

        t = df.get_data()
        nb_foyer_annee=dict()
        data_consommation_energie = dict()
        moyenne_consommation_energie=dict()
        #Recuperation du nombre de foyers par annee et un total de la consommation energetique chaque annee pour ensuite faire une moyenne 
        for i in t["results"]:
            if (i["annee_construction"] in nb_foyer_annee and i["consommation_energie"]>0):
                nb_foyer_annee[i["annee_construction"]] += 1
                data_consommation_energie[i["annee_construction"]] += i["consommation_energie"]

            else:
                nb_foyer_annee[i["annee_construction"]] = 1
                data_consommation_energie[i["annee_construction"]] = i["consommation_energie"]



        # moyenne de l estimation de consomation energetique par foyer par année 
        for i in sorted(nb_foyer_annee.keys()):
            if(begin_year<=i<=end_year):
                moyenne_consommation_energie[i]= data_consommation_energie[i]/nb_foyer_annee[i]

        self.figHist2 = px.histogram(x=moyenne_consommation_energie.keys(),
                                     y=moyenne_consommation_energie.values(),range_x=(begin_year,end_year),labels={"x": "Année de construction","y": "Estimation Consommation énergétique en kWhEP/m² "})

    def get_histo2(self):
        return self.figHist2
