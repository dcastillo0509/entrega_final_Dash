import os
os.chdir(os.path.dirname(__file__))

import dash
import dash_bootstrap_components as dbc
from dash import html, dcc, dash_table
import plotly.graph_objs as go
from backend.granulometria import granulometria
#importa las librerías necesarias


centro=dbc.Container([
      #crea la variable derecho y en ella un Container
      html.H1('Datos del Proyecto', style={'color':'#17242d'}),#Crea un titulo 1 y define el color del texto
      html.Hr(),#añade un espacio

      html.Label('Ingrese Peso Retenido', style={'color':'#17242d'}), 
    dash_table.DataTable(
        id='tabla_granulometria',
        columns=[
            {'name': 'Malla', 'id': 'Malla','editable': False},
            {'name': 'Abertura', 'id': 'Abertura','editable': False},
            {'name': 'Retenido', 'id': 'Retenido', 'editable': True},
            {'name': 'Retenido_acum', 'id': 'Retenido_acum', 'editable': False},
            {'name': 'Pasa', 'id': 'Pasa', 'editable': False},
            {'name': 'Por_Pasa', 'id': 'Por_Pasa', 'editable': False},
            ],
            data=granulometria.to_dict('records')
            ),
            dcc.Graph(id='granulometria_plot'),

            html.Label('Ingrese Datos Adicionales:', style={'color': '#17242d'}),
            #Se crea una etiqueta (texto) y define el color
            html.Br(),#añade un espacio
            html.Label('Límite Liquido: ', style={'color': '#17242d'}),
            #Se crea una etiqueta (texto) y define el color
            dcc.Input(id='limLiquido', value="40", type='number', min=15, max=60),
            #se crea un Input con identificador, valor por defecto, tipo numero, rango
            html.Br(),#añade un espacio
            html.Label('Índice de Plasticidad: ', style={'color': '#17242d'}),
            #Se crea una etiqueta (texto) y define el color
            dcc.Input(id='indicePlasticidad', value="10", type='number', min=7, max=17),
            #se crea un Input con identificador, valor por defecto, tipo numero y rango
            html.Br(),
])


def generate_granulometria_plot():
    trace = go.Scatter(
        x=granulometria['Abertura'][0:11],
        y=granulometria['Por_Pasa'][0:11],
        mode='lines',
        line=dict(color='black', width=2),
        name='Curva Granulométrica'
    )
    
    layout = go.Layout(
        title='Curva Granulométrica',
        xaxis=dict(
            title='Tamiz (mm)',
            type='log',
            autorange=True
        ),
        yaxis=dict(
            title='Porcentaje Pasa Acumulado %',
            range=[0, 100]
        )
    )

    return {'data': [trace], 'layout': layout}