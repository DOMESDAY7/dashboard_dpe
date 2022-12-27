import plotly.express as px
from Dataset import Dataset
from collections import namedtuple

# t = Dataset(select=("annee_construction", "classe_estimation_ges",
            # "estimation_ges"), size=10000)
# print(t.dumpURL())
# t = t.get_data()
# print(sorted((k,sorted(v.items()))for k,v in t.items))


class Histogramme:
    def __init__(self,df, year=2020):
        t=df.get_data()
        dannee = dict()
        nbEchantillon = 0
        print(nbEchantillon)
        nbechantillon = 0
        datages = dict()
        moyenneges = dict()
        dannee = dict()

        # recuperation du nombre de foyers par annee de construction et un total des estimations ges pour faire la moyenne ensuite
        for i in t["results"]:
            if (i["annee_construction"] in dannee):
                dannee[i["annee_construction"]] += 1
                datages[i["annee_construction"]] += i["estimation_ges"]
                # nbechantillon2=nbechantillon2+1
            else:
                dannee[i["annee_construction"]] = 1
                datages[i["annee_construction"]] = i["estimation_ges"]
                # nbechantillon2=nbechantillon2+1


# moyenne de l estimation GES par foyer par année 
        for i in sorted(dannee.keys()):
            if(1950<=i<=year):
                moyenneges[i]= datages[i]/dannee[i]
                print(i,dannee[i],moyenneges[i])
                nbechantillon+=dannee[i]
        

        print(nbechantillon)

        self.figHist = px.histogram(x=moyenneges.keys(),
                        y=moyenneges.values(),range_x=(1950,year),title="Estimation GES par foyer en Kg eq CO2/m².an",labels={"x": "Année de construction","y": "Estimation du GES"})

    def get_histo(self):
        return self.figHist
