from dash import html, dcc
import plotly.express as px
import pandas as pd
import dash_extensions.enrich as enrich

# Register the page
enrich.register_page(__name__, path="/vehicle-weight-range")

# Load vehicle data
vehicle_data = pd.read_csv("data/EV_Fleet_Project_DataFinal.csv")

# Create scatter plot: Gross Vehicle Weight vs. Electric Range
fig = px.scatter(
    vehicle_data,
    x="Gross Vehicle Weight (GVWR)",  # Replace with the exact column name
    y="Electric Range",               # Replace with the exact column name
    color="Make",
    title="Gross Vehicle Weight vs Electric Range",
    labels={"Gross Vehicle Weight (GVWR)": "Gross Vehicle Weight (kg)", "Electric Range": "Electric Range (km)"}
)

# Page layout
layout = html.Div([
    html.H2("Gross Vehicle Weight vs Electric Range"),
    dcc.Graph(figure=fig),
])
