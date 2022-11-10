import plotly.express as px
from dash import Dash, dcc, html, Input, Output
# import requests as req
# url = "https://koumoul.com/data-fair/api/v1/datasets/dpe-france/geo_agg"
# resp =req.get(url)
# print(resp.text)

from urllib.request import urlopen
import json

from Dataset import Dataset
with urlopen('https://raw.githubusercontent.com/plotly/datasets/master/geojson-counties-fips.json') as response:
    counties = json.load(response)

import pandas as pd
df = pd.read_csv("https://raw.githubusercontent.com/plotly/datasets/master/fips-unemp-16.csv",
                 dtype={"fips": str})

app  = Dash ( __name__ )
app.layout = html.Div([dcc.Graph(id='graph'),])


@app.callback(Output('graph', 'figure'), [Input('graph', 'clickData')])
def display_map(clickData):
    fig = px.choropleth_mapbox(df, 
                            geojson=counties,
                            locations='fips',
                            # color='unemp',
                            color_continuous_scale="Viridis",
                            range_color=(0, 12),
                            mapbox_style="carto-positron",
                            zoom=6, center={"lat": 47.35930910668562, "lon": 2.1092153156534095},
                            opacity=0.5,
                            # labels={'unemp': 'unemployment rate'}
                            )
    fig.update_layout(margin={"r": 0, "t": 0, "l": 0, "b": 0})
    return fig

app.run_server(debug=True)

