import plotly.express as px
from Dataset import Dataset


class Histogramme:
    """
    To create an histogramme on an average of the GES emissions by year
    """
    def __init__(self,df, year=2020, begin_year=1950):
        t=df.get_data()
        nb_foyer_annee = dict()
        nbechantillon = 0
        data_totale_ges = dict()
        moyenne_ges_foyer = dict()
        nb_foyer_annee = dict()

        # recuperation du nombre de foyers par annee de construction et un total des estimations ges pour faire la moyenne ensuite
        for i in t["results"]:
            if (i["annee_construction"] in nb_foyer_annee):
                nb_foyer_annee[i["annee_construction"]] += 1
                data_totale_ges[i["annee_construction"]] += i["estimation_ges"]
            else:
                nb_foyer_annee[i["annee_construction"]] = 1
                data_totale_ges[i["annee_construction"]] = i["estimation_ges"]


        # moyenne de l estimation GES par foyer par année 
        for i in sorted(nb_foyer_annee.keys()):
            if(begin_year<=i<=year):
                moyenne_ges_foyer[i]= data_totale_ges[i]/nb_foyer_annee[i]
                nbechantillon+=nb_foyer_annee[i]
        #Formation d un histogramme avec les annees en abscisses et les moyennes de GES en ordonnées
        self.figHist = px.histogram(x=moyenne_ges_foyer.keys(),
                        y=moyenne_ges_foyer.values(),range_x=(begin_year,year),labels={"x": "Année de construction","y": "Estimation GES en Kg eq CO2/m² "})

    def get_histo(self):
        """
        Return an histogramme
        """
        return self.figHist
