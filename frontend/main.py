import dash #importa dash
import dash_bootstrap_components as dbc #importa los componentes bootstrap de dash como dbc
from dash import html #De dash importa html

#importamos el frontend

from .navegador.navegador import navegador #importa container de navegador
from .centro.centro import centro #importa container de centro
from .inferior.inferior import inferior #importa container de inferior

imagen_fondo = 'url("https://images.unsplash.com/photo-1617634667039-8e4cb277ab46?auto=format&fit=crop&q=80&w=1000&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxzZWFyY2h8Mnx8bmF0dXJhbGV6YSUyMHBhaXNhamV8ZW58MHx8MHx8fDA%3D")'
#crea variable con el url de la imagen de fondo

layout=dbc.Container([ #en la variable layout, crea container de toda la página web
    dbc.Row([ #crea una fila
        dbc.Col(navegador, md=12, style={'background-color': 'gray'}), 
        #crea columna con navegador espacio de 12 y color de fondo gris
        dbc.Col(centro, md=12, style={'background-image': imagen_fondo,  
        #crea columna con derecho espacio de 6 y la imagen de fondo
                    'background-size': 'cover', # Ajusta el tamaño de la imagen
                    'background-repeat': 'no-repeat'}),
        dbc.Col(inferior, md=12, style={'background-color': 'gray'}),
        #crea columna con inferior espacio de 12 y color de fondo gris
    ])
])