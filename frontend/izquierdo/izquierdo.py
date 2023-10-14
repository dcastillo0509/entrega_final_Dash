import dash
import dash_bootstrap_components as dbc
from dash import html, dcc
#importa las lirerías necesarias

izquierdo=dbc.Container([#crea la variable izquierdo y en ella un Container
    dbc.Row([#crea una fila
        html.Br(),#añade un espacio
        dbc.Col(html.H3("1"), md=1, style={'color':'white', 'background-color':'#17242d'}),
        #crea una columna con titulo 3, espacio 1, define color de texto y fondo
        html.Hr(),#añade un espacio
        dbc.Col(html.H3("2"), md=1, style={'color':'white', 'background-color':'#17242d'}),
        #crea una columna con titulo 3, espacio 1, define color de texto y fondo
        html.Hr(),#añade un espacio
    ])
])