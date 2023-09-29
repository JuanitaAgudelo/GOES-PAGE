import dash
from dash import html, dcc, callback, Input, Output


dash.register_page(__name__)

layout = html.Div(children=[
    html.H2(children='This is our LST page', className='H2'),
    html.Div(html.Img(src="assets/LST.gif", className="cropped"), style={'margin-left': '20%'}),
    html.Div(children='''
        This is our LST page content.
    '''),

])

