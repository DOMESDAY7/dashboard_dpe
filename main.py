from dash import dcc, html, Input, Output
import plotly.express as px
import dash

app = dash.Dash(__name__)


app.layout = html.Div([
    html.H1('DPE in France'),
    
    html.Div([
        html.Div([html.Div([html.H3("Carte de la France")], className="card-header"), html.P("Select a candidate:"),dcc.Graph(id="map"), dcc.RadioItems(
            id='candidate',
            options=["Joly", "Coderre", "Bergeron"],
            value="Coderre",
            inline=True
        ), ], className="card"),
        html.Div([html.Div([html.H3("Histograme par commune")],
                 className="card-header"), dcc.Graph(id="histograme")], className="card"),
    ], id="globalContainer"),

])


@app.callback(
    Output("histograme", "figure"),
    Input("candidate", "value")
)
def display_histograme(candidate):
    fig_histograme = px.bar(x=["a", "b", "c"], y=[1, 3, 2])
    return fig_histograme


@app.callback(
    Output("map", "figure"),
    Input("candidate", "value"))
def display_choropleth(candidate):
    df = px.data.election()  # replace with your own data source
    geojson = px.data.election_geojson()
    fig = px.choropleth(
        df, geojson=geojson, color=candidate,
        locations="district", featureidkey="properties.district",
        projection="mercator", range_color=[0, 6500])
    fig.update_geos(fitbounds="locations", visible=False)
    fig.update_layout(margin={"r": 0, "t": 0, "l": 0, "b": 0})
    return fig


app.run_server(debug=True)
