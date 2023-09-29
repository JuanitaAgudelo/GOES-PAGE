from dash import Dash, callback, html, dcc, dash_table, Input, Output, State, MATCH, ALL, page_registry, page_container

import dash_bootstrap_components as dbc

import pandas as pd
import plotly.graph_objs as go
from sklearn import datasets
from sklearn.cluster import KMeans
import os



app = Dash(__name__,external_stylesheets=[dbc.themes.BOOTSTRAP], use_pages=True)

sidebar = html.Div(
    [
    html.H3('Productos'),
    html.Hr(),
    html.P('Los productos son extraídos de datos del satelite GOES, puedes elegir entre temperatura, radianza o obervar las relaciones de temperatura', style={"font-size": "15px"}),
    dbc.Nav(
            [
                dbc.NavLink(page['name'], href=page['path']) 
                for page in page_registry.values()
        ],
        vertical=True,
        pills=True,
        )
    ], className="sidebar"
)

app.layout = html.Div(
    [
        sidebar,
        html.Div([
        html.Img(src="assets/FACOM-logo-complete.jpg"), 
        html.H2("Imagenes Satelitales Colombia"),
        html.Img(src="assets/logo_fcen.png"), 
        ],  className='image-container'),
        page_container
    ], className="g-0"
)


if __name__ == "__main__":
    app.run_server(debug=True)


#http://www.pronosticosyalertas.gov.co/Goes-portlet/index.html
