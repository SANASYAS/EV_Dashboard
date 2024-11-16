from dash import Dash, html
import dash_bootstrap_components as dbc
import dash_extensions.enrich as enrich  # Enhances multi-page functionality

# Initialize Dash app
app = enrich.Dash(__name__, suppress_callback_exceptions=True, use_pages=True)

# Navigation Bar
navbar = dbc.NavbarSimple(
    children=[
        dbc.NavLink("Vehicle Weight vs Electric Range", href="/vehicle-weight-range", active="exact"),
        dbc.NavLink("Electric Range vs Battery Capacity", href="/electric-range-bc", active="exact"),
    ],
    brand="Fleet Dashboard",
    color="primary",
    dark=True,
)

# App Layout
app.layout = html.Div([
    navbar,
    enrich.page_container  # Automatically handles page content switching
])

if __name__ == '__main__':
    app.run_server(debug=True)
