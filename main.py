from dash import dcc, html, Output, Input
import plotly.express as px
import dash
#from histograme import figHist
from histograme import Histogramme
from histogramme2 import figHist2
#from histograme import nbechantillon
import pandas as pd
from map import DpeMap  # import the map
from faq import faqContent  # import the faq content
from Dataset import Dataset

app = dash.Dash(__name__)

data = Dataset(select=("annee_construction","latitude", "longitude",
               "classe_estimation_ges","estimation_ges","geo_adresse"), size=10000)
histo= Histogramme(data,year=1980)
histo=histo.get_histo()

data = pd.DataFrame(data.get_data()["results"])
#rename the column to be more readable
data.rename(columns={"classe_estimation_ges": "Classe consommation d'énergie"}, inplace=True)
data.rename(columns={"geo_adresse": "Adresse"}, inplace=True)
print(data)

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
                    html.P('Nombre d\'échantillon : '),
                ]),
                html.Div([
                    html.Div([html.Div([html.H3("Estimation GES par foyer en Kg eqCO2/m².an"),
                        dcc.RadioItems(
                        id='candidate',
                        options=["Par Région", "Par Annee"],
                        value="Coderre",
                        inline=True
                    ),
                        ], className="card-header"),
                        dcc.Graph(id="figurehist",figure=histo, className="graph"), 
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
    Output("figurehist","figure"),
    Input("year","value")
)
def testvalgraph(input_value):
    print(input_value)
    fighist.figure.range_x=(1950,input_value)

    


app.run_server(debug=True)
