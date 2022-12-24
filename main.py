from dash import dcc, html, Input, Output
import plotly.express as px
import dash
from histograme import figHist
from histogramme2 import figHist2
from histograme import nbEchantillon
import pandas as pd
from map import DpeMap  # import the map
from faq import faqContent  # import the faq content
from Dataset import Dataset

app = dash.Dash(__name__)

data = Dataset(select=("latitude", "longitude",
               "classe_estimation_ges"), size=100)

data = pd.DataFrame(data.get_data()["results"])


figMap = DpeMap(data)
figMap = figMap.get_map()


githubIcon = "https://external-content.duckduckgo.com/iu/?u=https%3A%2F%2Fpngimg.com%2Fuploads%2Fgithub%2Fgithub_PNG40.png&f=1&nofb=1&ipt=92afafb5c28685482c8d684e15bfbbfd6e0b2cf2df06fe12edb86b7b4cf134e4&ipo=images"


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
                    html.Div([html.Div([html.H3("Estimation GES par foyer en Kg eqCO2/m².an"),
                                        dcc.RadioItems(
                        id='candidate',
                        options=["Joly", "Coderre", "Bergeron"],
                        value="Coderre",
                        inline=True
                    )], className="card-header"),
                        dcc.Graph(figure=figHist, className="graph")],
                        className="card hist1"),
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
                *faqContent
            ], className="faq")
        ]),

        # Footer
        html.Footer([

            html.Div([
                html.A([html.Img(src=githubIcon),
                        "Mathieu Andriamiraho"], href="https://github.com/DOMESDAY7", className="github"),

                html.A([html.Img(src=githubIcon),
                        "Angelo Giordano"], href="https://github.com/agiordanoge1", className="github")

            ], className="containerGithub")

        ])


    ])

], className="wraper")

# app.callback(
#     Output("fighist"),
#     Input('type')
# )


# def testvalgraph(type):
#     if (type == "Par Region"):
#         fig = figHist
#     elif (type == "Par Annee"):
#         fig = figHist2
#     return fig


app.run_server(debug=True)
