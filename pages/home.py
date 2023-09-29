import dash 
from dash import dcc, html

dash.register_page(__name__, path='/')

layout = html.Div(
    [
        html.Div(html.Img(src="assets/img_sat_colombia5.gif", className="cropped"), style={'margin-left': '20%'}),
        html.Div(html.P('Combinación de imágenes de radianza ABI banda 2 con longitud de onda de 0.64 um, ABI banda 3'), className='centrado'),
        html.Div(html.P('con longitud de onda de 0.87 y ABI banda 1 con longitud de onda 0.47 um'), className='centrado')
        ]
)