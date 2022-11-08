import requests as req
url = "https://koumoul.com/data-fair/api/v1/datasets/dpe-france/geo_agg"
resp =req.get(url)
print(resp.text)