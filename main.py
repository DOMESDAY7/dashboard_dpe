from dash import dcc, html, Output, Input
import plotly.express as px
import dash
#from histograme import figHist
from model_histogramme import Histogramme
from model_histogramme2 import Histogramme2
#from histograme import nbechantillon
import pandas as pd
from model_dpe_map import DpeMap  # import the map
from faq import faqContent  # import the faq content
from Dataset import Dataset
from controller_dpe_map import figMap  # import the map
from controller_histogramme import histo  # import the histogram
from controller_histogramme2 import histo2  # import the histogram2

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
                    html.H1('DPE en France'),
                    html.P('Nombre d\'échantillon : '),
                ]),
                html.Div([
                    html.Div([html.Div([html.H3("Estimation GES par foyer en Kg eqCO2/m².an"),
                                        dcc.RadioItems(
                        id='choix',
                        options=["Par Région", "Par Année"],
                        value="Par Année",
                        inline=True
                    ),
                    ], className="card-header"),
                        dcc.Graph(id="figurehist", className="graph"),
                        dcc.Slider(id="year", min=1950, max=2020, value=2020,
                                   marks={1950: '1950', 2020: '2020'})],
                        className="card hist1"),
                    html.Div([html.Div([html.H3("Carte de la France"), dcc.RadioItems(
                        id="mapDataRadio",
                        options=[]
                    )],
                        className="card-header"),
                        dcc.Graph(figure=figMap)], className="card"),
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


@app.callback(
    Output("figurehist", "figure"),
    Input("year", "value"),
    Input("choix", "value")
)
def testvalgraph(input_value, input_value2):
    print(input_value, input_value2)
    if (input_value2 == "Par Année"):
        figure = histo
    else:
        figure = histo2
    return figure


app.run_server(debug=True)
