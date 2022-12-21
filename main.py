from dash import dcc, html, Input, Output
import plotly.express as px
import dash
from map import figMap
from histograme import figHist2
from histograme import nbechantillon
import dash_leaflet as dl
app = dash.Dash(__name__)


app.layout = html.Div([
    html.H1('DPE en France'),
    html.Div([
        html.Div([html.Div([html.H3("Estimation GES par foyer en Kg eqCO2/m².an"), dcc.RadioItems(
            id='candidate',
            options=["Joly", "Coderre", "Bergeron"],
            value="Coderre",
            inline=True
        )], className="card-header"), dcc.Graph(figure=figHist2)], className="card hist1"),
        html.Div([html.Div([html.H3("Carte de la France")], className="card-header"), figMap], className="card map"),
    ], className="globalContainer"),
])

app.run_server(debug=True)
