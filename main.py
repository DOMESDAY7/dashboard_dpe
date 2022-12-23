from dash import dcc, html, Input, Output
import plotly.express as px
import dash
from map import figMap
# from histograme import figHist
from histograme import figHist2
from histogramme2 import figHist
from histograme import nbechantillon

app = dash.Dash(__name__)


app.layout = html.Div([
    html.H1('DPE in France'),

    html.Div([
        # html.Div([html.Div([html.H3("Histograme par commune")], className="card-header"), html.P("Select an histogram: ("+str(nbechantillon)+" échantillons)"), dcc.Graph(figure=figHist), dcc.RadioItems(
        #     id='candidate',
        #     options=["Joly", "Coderre", "Bergeron"],
        #     value="Coderre",
        #     inline=True
        # ), ], className="card"),
        html.Div([html.Div([html.H3("Estimation GES par foyer en Kg eqCO2/m².an")], className="card-header"), html.P("Select an histogram: ( "+str(nbechantillon)+"échantillons)"), dcc.Graph(figure=testvalgraph(type)), dcc.RadioItems(
            id='type',
            options=["Par Region", "Par Annee"],
            inline=True
        ), ], className="card"),
        html.Div([html.Div([html.H3("Carte de la France")],
                 className="card-header"), dcc.Graph(figure=figMap)], className="card"),
    ], id="globalContainer"),

])

app.callback(
    Output("fighist"),
    Input('type')
)
def testvalgraph(type) :
    if(type=="Par Region") :
        fig=figHist
    elif(type=="Par Annee") :
        fig=figHist2
    return fig

app.run_server(debug=True)
