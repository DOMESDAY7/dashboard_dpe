from dash import dcc, html, Output, Input
import plotly.express as px
import dash
from model_histogramme import Histogramme
import pandas as pd
from model_dpe_map import DpeMap  # import the map
from faq import faqContent  # import the faq content
from Dataset import Dataset
from controller_dpe_map import figMap  # import the map
from controller_histogramme import update  # import the histogram

app = dash.Dash(__name__)

# github icon
githubIcon = "https://external-content.duckduckgo.com/iu/?u=https%3A%2F%2Fpngimg.com%2Fuploads%2Fgithub%2Fgithub_PNG40.png&f=1&nofb=1&ipt=92afafb5c28685482c8d684e15bfbbfd6e0b2cf2df06fe12edb86b7b4cf134e4&ipo=images"


app.layout = html.Div([


    html.Main([
        # content dashboard
        html.Section([
            html.Div([
                # header
                html.Div([
                    html.H1('Diagnostic de Performance Energétique (DPE) en France'),
                ]),
                html.Div([
                    html.Div([html.Div([
                        html.H3(
                            "Estimation Gaz à Effet de Serre par foyer\n en fonction de l'année de construction"),
                    ], className="card-header"),
                        dcc.Graph(id="figurehist", className="graph"),
                        html.H4("Choix de l'intervalle d'année :"),
                        dcc.Slider(id="year_GES", min=1950, max=2020, value=2020,
                                   marks={1950: '1950', 1960: '1960', 1970: '1970', 1980: '1980', 1990: '1990', 2000: '2000', 2010: '2010', 2020: '2020'})],
                        className="card hist1"),
                    html.Div([html.Div([html.H3("Carte de la France"), dcc.RadioItems(
                        id="mapDataRadio",
                        options=[]
                    )],
                        className="card-header"),
                        dcc.Graph(figure=figMap),
                        ], className="card"),
                ], className="dashboardItemsContainer"),
                html.Div([html.Div([
                    html.H3(
                          "Estimation Consommation énergétique par foyer en fonction de l'année de construction"),
                ], className="card-header"),
                    dcc.Graph(id="figurehist2", className="graph"),
                    html.H4("Choix de l'intervalle d'année :"),
                    dcc.Slider(id="year_energie", min=1950, max=2020, value=2020,
                                   marks={1950: '1950', 1960: '1960', 1970: '1970', 1980: '1980', 1990: '1990', 2000: '2000', 2010: '2010', 2020: '2020'})],
                    className="card hist2"),

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


@app.callback(
    Output("figurehist", "figure"),
    Output("figurehist2", "figure"),
    Input("year_GES", "value"),
    Input("year_energie", "value"),
)
def callback_slider(year_GES,year_energie):
    print(year_GES,year_energie)
    # if (input_value2 == "Par Année"):
    stock_histo, stock_histo2 = update(year_GES=year_GES,year_energie=year_energie)
    figure = stock_histo
    figure2 = stock_histo2
    # else:
    #     figure = histo2
    return figure,figure2


app.run_server(debug=True)
