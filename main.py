import requests as req
url = "https://data.ademe.fr/data-fair/api/v1/datasets/dpe-france"
resp =req.get(url)
print(resp.text)