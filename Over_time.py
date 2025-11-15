import plotly.express as px 

df = px.data.gapminder()
fig = px.choropleth(
    df,
    locations="iso_alpha",
    color="lifeExp",
    hover_name="country",
    animation_frame="year",
    color_continuous_scale=px.colors.sequential.Plasma,
    title="Global Life Expectancy Over Time"
)
fig.show()