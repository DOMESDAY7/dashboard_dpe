import plotly.express as px
from Dataset import Dataset
from collections import namedtuple


# t = Dataset(select=("annee_construction", "tv016_departement_code",
#             "classe_estimation_ges", "estimation_ges"), size=10000)

class Histogramme2:
    def __init__(self,df, year=2020):

        t = df.get_data()
        dannee=dict()
        data_consommation_energie = dict()
        moyenne_consommation_energie=dict()

        nbechantillon = 0
        nbechantillon2 = 0
        compteur=0
        test=dict()

        for i in t["results"]:
            if (i["annee_construction"] in dannee and i["consommation_energie"]>0):
                dannee[i["annee_construction"]] += 1
                data_consommation_energie[i["annee_construction"]] += i["consommation_energie"]

            else:
                dannee[i["annee_construction"]] = 1
                data_consommation_energie[i["annee_construction"]] = i["consommation_energie"]



# moyenne de l estimation GES par foyer par année 
        for i in sorted(dannee.keys()):
            if(1950<=i<=year):
                moyenne_consommation_energie[i]= data_consommation_energie[i]/dannee[i]
                nbechantillon+=dannee[i]

        self.figHist2 = px.histogram(x=moyenne_consommation_energie.keys(), y=moyenne_consommation_energie.values(),range_x=(1950,year),labels={"x": "Année de construction","y": "Estimation Consommation énergétique en kWhEP/m² "})

    def get_histo2(self):
        return self.figHist2
