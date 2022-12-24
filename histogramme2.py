import plotly.express as px
from Dataset import Dataset


t = Dataset(select=("annee_construction", "tv016_departement_code",
            "classe_estimation_ges", "estimation_ges"), size=10000)
t = t.get_data()

A = 1
B = 1
C = 1
D = 1
E = 1
F = 1
G = 1

Stock = 0
dges = dict()
dgesbyregion = dict()
dgesbyregion["IDF"] = 0
dgesbyregion["ARA"] = 0
dgesbyregion["BFR"] = 0
dgesbyregion["BRE"] = 0
dgesbyregion["CVL"] = 0
dgesbyregion["GE"] = 0

departlocalisation = dict()
dlocalisation = dict()
dlocalisation["IDF"] = 0
dlocalisation["ARA"] = 0
dlocalisation["BFR"] = 0
dlocalisation["BRE"] = 0
dlocalisation["CVL"] = 0
dlocalisation["GE"] = 0


IDF = ("75", "77", "78", "91", "92", "93", "94", "95")
ARA = ("01", "03", "07", "15", "26", "38", "42", "43", "63", "69", "73", "74")
BFR = ("21", "25", "39", "58", "70", "71", "89", "90")
BRE = ("22", "29", "35", "56")
CVL = ("18", "28", "36", "37", "41", "45")
GE = ("08", "10", "51", "52", "54", "55", "57", "67", "68", "88")

nbechantillon = 0
nbechantillon2 = 0


# recuperation du nombre de foyers par annee de construction et un total des estimations ges pour faire la moyenne ensuite
for i in t["results"]:
    # print(i)
    if (i["tv016_departement_code"] in departlocalisation):
        departlocalisation[i["tv016_departement_code"]] += 1
        dges[i["tv016_departement_code"]] += i["estimation_ges"]
        nbechantillon2 = nbechantillon2+1
    else:
        departlocalisation[i["tv016_departement_code"]] = 1
        dges[i["tv016_departement_code"]] = i["estimation_ges"]
        nbechantillon2 = nbechantillon2+1


# for i in sorted(departlocalisation.keys()):
#     print(i,departlocalisation[i], dges[i])
#     nbechantillon2=nbechantillon2+1

# echantillonage avec des tranches d annees pour condenser les donnees en abscisses
for i in sorted(departlocalisation.keys()):

    if (i in IDF and dges[i] > 0):
        dlocalisation["IDF"] += departlocalisation[i]
        dgesbyregion["IDF"] += dges[i]
    elif (i in ARA and dges[i] > 0):
        dlocalisation["ARA"] += departlocalisation[i]
        dgesbyregion["ARA"] += dges[i]
    elif (i in BFR and dges[i] > 0):
        dlocalisation["BFR"] += departlocalisation[i]
        dgesbyregion["BFR"] += dges[i]
    elif (i in BRE and dges[i] > 0):
        dlocalisation["BRE"] += departlocalisation[i]
        dgesbyregion["BRE"] += dges[i]
    elif (i in CVL and dges[i] > 0):
        dlocalisation["CVL"] += departlocalisation[i]
        dgesbyregion["CVL"] += dges[i]
    elif (i in GE and dges[i] > 0):
        dlocalisation["GE"] += departlocalisation[i]
        dgesbyregion["GE"] += dges[i]


print(nbechantillon)
# print(i,dannee[i])
# moyenne des estimations ges total/nombre de foyers
moyenne = dict()
moyenne["IDF"] = dgesbyregion["IDF"]/dlocalisation["IDF"]
moyenne["ARA"] = dgesbyregion["ARA"]/dlocalisation["ARA"]
moyenne["BFR"] = dgesbyregion["BFR"]/dlocalisation["BFR"]
moyenne["BRE"] = dgesbyregion["BRE"]/dlocalisation["BRE"]
moyenne["CVL"] = dgesbyregion["CVL"]/dlocalisation["CVL"]
moyenne["GE"] = dgesbyregion["GE"]/dlocalisation["GE"]


figHist2 = px.histogram(x=["Ile-De-France", "Auvergne-Rhône-Alples", "Bourgogne-Franche-Comté", "Bretagne", "Centre-Val-de-Loire",
                       "Grand-Est"], y=[moyenne["IDF"], moyenne["ARA"], moyenne["BFR"], moyenne["BRE"], moyenne["CVL"], moyenne["GE"]])
