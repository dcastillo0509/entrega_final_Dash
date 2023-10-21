import os
os.chdir(os.path.dirname(__file__))

import dash_bootstrap_components as dbc
from dash import html, dcc
#importa las librerías necesarias

inferior=dbc.Container([#crea la variable inferior y en ella un Container
    dbc.Row([#crea una fila
        html.Hr(),#añade un espacio
        dbc.Col(html.H3("Clasificación SUCS (Sistema Unificado de Clasificación de Suelos)"), 
                md=6, style={'background-color':'#45ad7e'}),
                #crea una columna con titulo 3, espacio 6 y define el color de fondo
        dbc.Col(dcc.Graph(id="plot_plasticity-chart"), md=12),
        #crea una columna con titulo 3, espacio 3, define el color del texto y fondo
        html.Hr(),#añade un espacio
    ])
])

