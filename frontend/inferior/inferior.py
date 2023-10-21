import os
os.chdir(os.path.dirname(__file__))

import dash
import dash_bootstrap_components as dbc
from dash import html, dcc
import pandas as pd
from operator import ipow
from matplotlib import axes
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker
import numpy as np
from dash import Dash, html, dcc, dash_table, Input, Output, callback
import plotly.tools as tls
import plotly.graph_objs as go
import backend.backend1 
#importa las librerías necesarias

inferior=dbc.Container([#crea la variable inferior y en ella un Container
    dbc.Row([#crea una fila
        html.Hr(),#añade un espacio
        dbc.Col(html.H3("Clasificación SUCS (Sistema Unificado de Clasificación de Suelos)"), 
                md=6, style={'background-color':'#45ad7e'}),
                #crea una columna con titulo 3, espacio 6 y define el color de fondo
        dbc.Col(plot_plasticity_chart),
        #crea una columna con titulo 3, espacio 3, define el color del texto y fondo
        html.Hr(),#añade un espacio
    ])
])

def plot_plasticity_chart(limLiquido, indicePlasticidad):
    if Tamiz_200 < 5:
        print()
        return

    fig, ax = plt.subplots()
    
    # Valores para la gráfica
    lineaAx = np.linspace(0, 100, 10)
    lineaAy = [0.73 * (i - 20) for i in lineaAx]
    lineaBx = np.linspace(0, 100, 10)
    lineaBy = [0.9 * (i - 8) for i in lineaAx]
    lineaCx = np.array([((4 + 8 * 0.9) / 0.9), ((4 + 20 * 0.73) / 0.73)])
    lineaCy = [4 for i in lineaCx]
    lineaDx = np.array([((7 + 8 * 0.9) / 0.9), ((7 + 20 * 0.73) / 0.73)])
    lineaDy = [7 for i in lineaCx]
    lineaEy = np.linspace(0, 100, 10)
    lineaEx = [ 50 for i in lineaEy ]
    
    plt.title("CARTA DE PLASTICIDAD", fontsize=18)

    # Rectas de clasificación
    plt.plot(lineaAx, lineaAy, label="Linea A", color="black")
    plt.text(82, 49, 'Línea A', size=12, rotation=35)
    plt.plot(lineaBx, lineaBy, label="Linea U", linestyle='--', color="black")
    plt.text(70, 60, 'Línea U', size=12, rotation=35)
    plt.plot(lineaCx, lineaCy, color="black", linestyle='--')
    plt.plot(lineaDx, lineaDy, linestyle='--', color="black")
    plt.plot(lineaEx, lineaEy, color="black")
    
    # Rellenar áreas entre las líneas
    plt.fill_between(lineaBx, lineaAy, lineaBy, color='peachpuff', alpha=1.0)
    plt.fill_between(lineaCx, lineaCy, lineaDy, color='red', alpha=0.2)
    plt.fill_between(lineaBx, lineaAy, color='cyan', alpha=0.2)
    
    # Configurar límites
    plt.xlim(0, 100)
    plt.ylim(0, 70)
    
    # Añadir texto a la gráfica
    ax.text(63, 43, "CH U OH", style="normal", fontsize=8, bbox={"facecolor": "white", "alpha": 0.4, "pad": 2})
    ax.text(63, 23, "MH U OH", style="normal", fontsize=8, bbox={"facecolor": "white", "alpha": 0.4, "pad": 2})
    ax.text(23, 23, "CL U OL", style="normal", fontsize=8, bbox={"facecolor": "white", "alpha": 0.4, "pad": 2})
    ax.text(35, 5, "ML U OL", style="normal", fontsize=8, bbox={"facecolor": "white", "alpha": 0.4, "pad": 2})
    ax.text(4, 7, "CL U ML", style="normal", fontsize=8, bbox={"facecolor": "none", "alpha": 0.4, "pad": 2})
    
    # Añadir el nombre de los ejes
    plt.scatter(limLiquido, indicePlasticidad, alpha=1, color="black")
    plt.xlabel("Límite líquido", fontsize=14)
    plt.ylabel("Índice de plasticidad", fontsize=14)
    
    plt.show()

# Llama a la función proporcionando los datos necesarios
plot_plasticity_chart(limLiquido, indicePlasticidad)