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


    html.Main([
        # content dashboard
        html.Section([
            html.Div([
                # header
                html.Div([
                    html.H1('DPE en France'),
                    html.P('Nombre d\'échantillon : '+str(nbEchantillon)),
                ]),
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
                ], className="dashboardItemsContainer")

            ], className="dashboard"),
        ]),


        # FAQ
        html.Section([
            html.Div([
                html.H3("FAQ"),
                html.Details([
                    html.Summary("D'ou proviennent les données ?"),
                    html.P(["Les données de ce dashboard proviennent d'une base de donnée réalisé par l'observatoire du DPE en France ",
                            html.A(
                                "ADEME.", href="https://www.data.gouv.fr/fr/organizations/ademe/")])], className="card"),
                html.Div(html.Details([html.Summary("Qu'est-ce que le DPE ?"),
                                       html.P("Le DPE est le diagnostique des performance énergétique, il sert principalement à évaluer la quantité d'énergie et de gaz à effet de serre d'un logement.")], className="card")),
                html.Div(html.Details([html.Summary("C'est indice est-il important ?"),
                                       html.P("Oui, bien évidemment l'indice de diagnostique des performances énergétique")], className="card"))
            ], className="faq")
        ]),

        # Footer
        html.Footer([

            html.Div([
                html.A([html.Img(src="https://external-content.duckduckgo.com/iu/?u=https%3A%2F%2Fpngimg.com%2Fuploads%2Fgithub%2Fgithub_PNG40.png&f=1&nofb=1&ipt=92afafb5c28685482c8d684e15bfbbfd6e0b2cf2df06fe12edb86b7b4cf134e4&ipo=images"),
                        "Mathieu Andriamiraho"], href="https://github.com/DOMESDAY7", className="github"),



                html.A([html.Img(src="https://external-content.duckduckgo.com/iu/?u=https%3A%2F%2Fpngimg.com%2Fuploads%2Fgithub%2Fgithub_PNG40.png&f=1&nofb=1&ipt=92afafb5c28685482c8d684e15bfbbfd6e0b2cf2df06fe12edb86b7b4cf134e4&ipo=images"),
                        "Angelo Giordano"], href="https://github.com/agiordanoge1", className="github")

            ], className="containerGithub")

        ])


    ])

], className="wraper")

app.run_server(debug=True)
