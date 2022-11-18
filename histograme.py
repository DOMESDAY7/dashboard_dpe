import plotly.express as px
from Dataset import Dataset


t = Dataset(select=("nom_methode_dpe","classe_estimation_ges"), size=10000)
t = t.getData()


d= dict()
for i in t["results"]:
    if(i["classe_estimation_ges"] in d):
        d[i["classe_estimation_ges"]] += 1
    else:
        d[i["classe_estimation_ges"]] = 1

print(d)

nbechantillon=0
nbechantillon=10000-d['N']
print(nbechantillon)




#total=total/10000




figHist = px.histogram(x=["A", "B", "C", "D","E","F","G"], y=[d['A'], d['B'], d['C'], d['D'], d['E'], d['F'],d['G']])
