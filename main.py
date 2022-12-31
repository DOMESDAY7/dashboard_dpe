from dash import dcc, html, Output, Input
import plotly.express as px
import dash
import pandas as pd
from model_dpe_map import DpeMap  # import the map
from faq import faqContent  # import the faq content
from Dataset import Dataset
from controller_dpe_map import figMap  # import the map
from controller_histogramme import update  # import the histogram

app = dash.Dash(__name__)

# github icon
githubIcon = "https://github.githubassets.com/images/modules/logos_page/GitHub-Mark.png"


app.layout = html.Div([


    html.Main([
        # content dashboard
        html.Section([
            html.Div([

                # header
                html.Div([
                    html.H1(
                        'Diagnostic de Performance Energétique (DPE) en France'),
                ]),

                # histogramme gaz effet de serre
                html.Div([
                    html.Div([html.Div([html.Div([
                        html.H3(
                            "Estimation Gaz à Effet de Serre par foyer en fonction de l'année de construction"),
                    ], className="card-header"),
                        dcc.Graph(id="figurehist", className="graph")],
                        className="card hist1"),
                        html.Div([
                            html.H4(["Choix de l'intervalle d'année :"],className="card-header_input"),
                            dcc.RangeSlider(min=1950, max=2020, value=[1950, 2020], step=10,
                                            marks={1950: '1950', 1960: '1960', 1970: '1970', 1980: '1980', 1990: '1990', 2000: '2000', 2010: '2010', 2020: '2020'}, id="year_GES",)
                        ], className="card")], className="containerCardHistogramme"),

                    # carte de france
                    html.Div([html.Div(html.H3("Carte de la France"),
                                       className="card-header"),
                              dcc.Graph(figure=figMap),
                              ], className="card"),
                ], className="dashboardItemsContainer"),

                # histogramme consommation energie
                html.Div([html.Div([html.Div(
                    html.H3(
                          "Estimation Consommation énergétique par foyer en fonction de l'année de construction\n"), className="card-header"),
                    dcc.Graph(id="figurehist2", className="graph")], className="card hist2"),
                    html.Div([
                        html.H4(["Choix de l'intervalle d'année :"],
                                className="card-header_input"),
                        dcc.RangeSlider(min=1950, max=2020, value=[1950, 2020], step=10,
                                        marks={1950: '1950', 1960: '1960', 1970: '1970', 1980: '1980', 1990: '1990', 2000: '2000', 2010: '2010', 2020: '2020'}, id="year_energie")], className="card")], className="containerCardHistogramme")


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
def callback_slider(year_GES, year_energie):
    print(year_GES, year_energie)
    begin_year_GES, end_year_GES = year_GES
    begin_year_energie, end_year_energie = year_energie
    stock_histo, stock_histo2 = update(end_year_GES=end_year_GES, begin_year_GES=begin_year_GES,
                                       begin_year_energie=begin_year_energie, end_year_energie=end_year_energie)
    figure_GES = stock_histo
    figure_energie = stock_histo2

    return figure_GES, figure_energie


app.run_server(debug=False)
