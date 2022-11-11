import requests as req
import plotly.express as px
url = "https://data.ademe.fr/data-fair/api/v1/datasets/dpe-france"
resp =req.get(url)
print(resp.text)

fig_histograme = px.bar(x=["a", "b", "c"], y=[1, 3, 2])
