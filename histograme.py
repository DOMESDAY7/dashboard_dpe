import plotly.express as px
from Dataset import Dataset


t = Dataset(select=("annee_construction","classe_estimation_ges"), size=100)
t = t.getData()


d= dict()
dannee=dict()

for i in t["results"]:
    if(i["classe_estimation_ges"] in d):
        d[i["classe_estimation_ges"]] += 1
    else:
        d[i["classe_estimation_ges"]] = 1

print(d)
print(t)

nbechantillon=0
nbechantillon=10000-d['N']
print(nbechantillon)

#for i in t["results"]:
    #if(i["annee_construction"] in dannee):
    #   dannee[i["annee_construction"]] += 1
    #else:
    #    dannee[i["annee_construction"]] = 1
preAnner = 0
for da in t["results"]:
    if da["annee_construction"] < preAnner:
        continue
    if(da["annee_construction"] in dannee):
        for i in t["results"]:
            preAnner = da["annee_construction"]+10
            if(da["annee_construction"]<i["annee_construction"]<da["annee_construction"]+10):
                    if(da["annee_construction"] in dannee):
                        dannee[da["annee_construction"]] += 1
                    else:
                        dannee[da["annee_construction"]] = 1
                

print(dannee)

#total=total/10000




#figHist = px.histogram(x=["A", "B", "C", "D","E","F","G"], y=[d['A'], d['B'], d['C'], d['D'], d['E'], d['F'],d['G']])

#figHist2 = px.histogram(x=["1950","1960"], y=[dannee['195'],dannee['1961']])
