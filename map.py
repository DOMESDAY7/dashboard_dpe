import plotly.graph_objects as go


class Map:
    """
    Class to create a map
    
    it a return a plotly.graph_objects.Figure

    Example :
    figMap = Map()
    figMap = figMap.getMap()

    """
    def __init__(self):
        self.fig = go.Figure()

    def getMap(self):
        """
        Returns a map
        """
        self.fig.update_layout(
            mapbox_style="open-street-map",
            mapbox_zoom=9, mapbox_center={"lat": 48.8566, "lon": 2.3522}
        )
        self.fig.update_layout(margin={"r": 0, "t": 0, "l": 0, "b": 0})
        return self.fig

    def setMarker(self, position, icon):
        """
        Add a marker on the map

        position : [lat,lon]
        icon : go.layout.mapbox.Marker

        Example :
        icon = go.layout.mapbox.Marker(
            size=14,
            color="red",
            opacity=0.7
        )

        """
        self.fig.add_trace(go.Scattermapbox(
            lat=[position[0]],
            lon=[position[1]],
            mode='markers',
            marker=icon
        ))
