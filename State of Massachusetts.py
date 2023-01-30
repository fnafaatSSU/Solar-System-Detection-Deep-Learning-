import plotly.express as px
import pandas as pd

df = pd.read_csv("/content/LISTALLCITIES.csv")

fig = px.scatter_mapbox(df,hover_name="Location",lat='Latitude',lon='Longitude')

fig.update_layout(mapbox_style="open-street-map")

fig.update_layout(
    title_x=0.5,
    title_y=0.95,
    title_text="State of Massachusetts",
    margin={"l": 0, "r": 0, "b": 0, "t": 80}
)

fig.show()
