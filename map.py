import plotly.express as px


class DpeMap:
    """
    Class to create a map
    it return a plotly.graph_objects.Figure

    Example :
    figMap = Map()
    figMap = figMap.getMap()

    """

    def __init__(self, df):

        self.figMap = px.scatter_mapbox(
            df, lat="latitude", lon="longitude", size_max=15, zoom=4, mapbox_style="carto-positron", color="Classe consommation d'énergie", hover_name="Adresse", hover_data=["Classe consommation d'énergie"], color_discrete_sequence=px.colors.cyclical.IceFire)

    def get_map(self):
        """
        Returns a map
        """
        return self.figMap
