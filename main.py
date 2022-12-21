from dash import dcc, html, Input, Output
import plotly.express as px
import dash
from histograme import figHist
from histograme import nbEchantillon
import dash_leaflet as dl
import pandas as pd
from map import Map

app = dash.Dash(__name__)

df = pd.read_csv(
    'https://raw.githubusercontent.com/plotly/datasets/master/earthquakes-23k.csv')

figMap = Map()
figMap = figMap.getMap()


app.layout = html.Div([
    html.H1('DPE en France'),
    html.P('Nombre d\'échantillon : '+str(nbEchantillon)),
    html.Div([
        html.Div([html.Div([html.H3("Estimation GES par foyer en Kg eqCO2/m².an"), dcc.RadioItems(
            id='candidate',
            options=["Joly", "Coderre", "Bergeron"],
            value="Coderre",
            inline=True
        )], className="card-header"), dcc.Graph(figure=figHist)], className="card hist1"),
        html.Div([html.Div([html.H3("Carte de la France")],
                 className="card-header"), 
                 dcc.Graph(figure=figMap)], className="card map"),
    ], className="global-container"),
], className="wraper")

app.run_server(debug=True)
