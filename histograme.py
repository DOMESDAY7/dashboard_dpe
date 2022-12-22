import plotly.express as px
from Dataset import Dataset


t = Dataset(select=("annee_construction","classe_estimation_ges","estimation_ges"), size=10000)
# print(t.dumpURL())
t = t.getData()
# print(sorted((k,sorted(v.items()))for k,v in t.items))


# d= dict()
dges=dict()
dgesbyten=dict()
dgesbyten["1700"]=0
dgesbyten["1900"]=0
dgesbyten["1950"]=0
dgesbyten["1970"]=0
dgesbyten["2000"]=0
dgesbyten["2010"]=0

dannee=dict()
danneetribyten=dict()
danneetribyten["1700"]=0
danneetribyten["1900"]=0
danneetribyten["1950"]=0
danneetribyten["1970"]=0
danneetribyten["2000"]=0
danneetribyten["2010"]=0

# for i in t["results"]:
#     if(i["classe_estimation_ges"] in d):
#         d[i["classe_estimation_ges"]] += 1
#     else:
#         d[i["classe_estimation_ges"]] = 1

# print(d)
# print(t)

nbechantillon=0
nbechantillon2=0
# nbechantillon=10000-d['N']
# print(nbechantillon)

#recuperation du nombre de foyers par annee de construction et un total des estimations ges pour faire la moyenne ensuite 
for i in t["results"]:
    if(i["annee_construction"] in dannee):
      dannee[i["annee_construction"]] += 1
      dges[i["annee_construction"]] += i["estimation_ges"]
      #nbechantillon2=nbechantillon2+1
    else:
       dannee[i["annee_construction"]] = 1
       dges[i["annee_construction"]] = i["estimation_ges"]
       #nbechantillon2=nbechantillon2+1
      

for i in sorted(dannee.keys()):
    print(i,dannee[i],dges[i])
    nbechantillon2=nbechantillon2+1

#echantillonage avec des tranches d annees pour condenser les donnees en abscisses
for i in sorted(dannee.keys()):
    if(1700<i<1900 and dges[i]>0):
      danneetribyten["1700"]+=dannee[i]
      dgesbyten["1700"]+=dges[i]
      nbechantillon=nbechantillon+dannee[i]
    elif(1900<=i<1950 and dges[i]>0):
      danneetribyten["1900"]+=dannee[i]
      dgesbyten["1900"]+=dges[i]
      nbechantillon=nbechantillon+dannee[i]
    elif(1950<=i<1970 and dges[i]>0):
      danneetribyten["1950"]+=dannee[i]
      dgesbyten["1950"]+=dges[i]
      nbechantillon=nbechantillon+dannee[i]
    elif(1970<=i<2000 and dges[i]>0):
      danneetribyten["1970"]+=dannee[i]
      dgesbyten["1970"]+=dges[i]
      nbechantillon=nbechantillon+dannee[i]
    elif(2000<=i<2010 and dges[i]>0):
      danneetribyten["2000"]+=dannee[i]
      dgesbyten["2000"]+=dges[i]
      nbechantillon=nbechantillon+dannee[i]  
    elif(2010<=i<2015 and dges[i]>0):
      danneetribyten["2010"]+=dannee[i]
      dgesbyten["2010"]+=dges[i]
      nbechantillon=nbechantillon+dannee[i] 
      

print(nbechantillon)      
    # print(i,dannee[i])
#moyenne des estimations ges total/nombre de foyers
moyenne=dict()
moyenne["1700"]=dgesbyten["1700"]/danneetribyten["1700"]
moyenne["1900"]=dgesbyten["1900"]/danneetribyten["1900"]
moyenne["1950"]=dgesbyten["1950"]/danneetribyten["1950"]
moyenne["1970"]=dgesbyten["1970"]/danneetribyten["1970"]
moyenne["2000"]=dgesbyten["2000"]/danneetribyten["2000"]
moyenne["2010"]=dgesbyten["2010"]/danneetribyten["2010"]


# print(danneetribyten["1700"])
# print(dannee)
# preAnner = 0
# for da in t["results"]:
#     if da["annee_construction"] < preAnner:
#         continue
#     if(da["annee_construction"] in dannee):
#         for i in t["results"]:
#             preAnner = da["annee_construction"]+10
#             if(da["annee_construction"]<i["annee_construction"]<da["annee_construction"]+10):
#                     if(da["annee_construction"] in dannee):
#                         dannee[da["annee_construction"]] += 1
#                     else:
#                         dannee[da["annee_construction"]] = 1
                

# print(dannee)

# #total=total/10000




# #figHist = px.histogram(x=["A", "B", "C", "D","E","F","G"], y=[d['A'], d['B'], d['C'], d['D'], d['E'], d['F'],d['G']])

figHist2 = px.histogram(x=["1700-1899","1900-1949","1950-1969","1970-2000","2000-2009","2010-2015"], y=[moyenne['1700'],moyenne['1900'],moyenne['1950'],moyenne["1970"],moyenne['2000'],moyenne["2010"]])
