from dash import html, dcc
import plotly.express as px
import pandas as pd
import dash_extensions.enrich as enrich

# Register the page
enrich.register_page(__name__, path="/electric-range-bc")

# Load vehicle data
vehicle_data = pd.read_csv("data/EV_Fleet_Project_DataFinal.csv")

# Create scatter plot: Electric Range vs Battery Capacity
fig = px.scatter(
    vehicle_data,
    x="Electric Range",         # Replace with the exact column name
    y="Battery Capacity",       # Replace with the exact column name
    color="Make",
    title="Electric Range vs Battery Capacity",
    labels={"Electric Range": "Electric Range (km)", "Battery Capacity": "Battery Capacity (kWh)"}
)

# Page layout
layout = html.Div([
    html.H2("Electric Range vs Battery Capacity"),
    dcc.Graph(figure=fig),
])
