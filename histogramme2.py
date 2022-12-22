import plotly.express as px
from Dataset import Dataset


t = Dataset(select=("annee_construction", "tv016_departement_code","classe_estimation_ges","estimation_ges"), size=10000)
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

departlocalisation=dict()
dlocalisation=dict()
dlocalisation["Paris"]=0
dlocalisation["Marseille"]=0
dlocalisation["t"]=0
dlocalisation["aris"]=0
dlocalisation["ris"]=0

dannee=dict()
danneetribyten=dict()
danneetribyten["1700"]=0
danneetribyten["1900"]=0
danneetribyten["1950"]=0
danneetribyten["1970"]=0
danneetribyten["2000"]=0
danneetribyten["2010"]=0

nbechantillon=0
nbechantillon2=0


#recuperation du nombre de foyers par annee de construction et un total des estimations ges pour faire la moyenne ensuite 
for i in t["results"]:
    print(i)
    if(i["tv016_departement_code"] in departlocalisation):
      departlocalisation[i["tv016_departement_code"]] += 1
      #dges[i["annee_construction"]] += i["estimation_ges"]
      nbechantillon2=nbechantillon2+1
    else:
       departlocalisation[i["tv016_departement_code"]] = 1
       #dges[i["annee_construction"]] = i["estimation_ges"]
       nbechantillon2=nbechantillon2+1
      

for i in sorted(departlocalisation.keys()):
    print(i,departlocalisation[i])
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
      

print(nbechantillon2)      
    # print(i,dannee[i])
#moyenne des estimations ges total/nombre de foyers
# moyenne=dict()
# moyenne["1700"]=dgesbyten["1700"]/danneetribyten["1700"]
# moyenne["1900"]=dgesbyten["1900"]/danneetribyten["1900"]
# moyenne["1950"]=dgesbyten["1950"]/danneetribyten["1950"]
# moyenne["1970"]=dgesbyten["1970"]/danneetribyten["1970"]
# moyenne["2000"]=dgesbyten["2000"]/danneetribyten["2000"]
# moyenne["2010"]=dgesbyten["2010"]/danneetribyten["2010"]


# figHist2 = px.histogram(x=["1700-1899","1900-1949","1950-1969","1970-2000","2000-2009","2010-2015"], y=[moyenne['1700'],moyenne['1900'],moyenne['1950'],moyenne["1970"],moyenne['2000'],moyenne["2010"]])
