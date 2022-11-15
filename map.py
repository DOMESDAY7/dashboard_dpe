import plotly.express as px

df = px.data.election()  # replace with your own data source
geojson = px.data.election_geojson()
figMap = px.choropleth(
    df, geojson=geojson,
    locations="district", featureidkey="properties.district",
    projection="mercator", range_color=[0, 6500])
figMap.update_geos(fitbounds="locations", visible=False)
figMap.update_layout(margin={"r": 0, "t": 0, "l": 0, "b": 0})
