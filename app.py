import dash #importa dash
import dash_bootstrap_components as dbc #importa los componentes bootstrap de das como dbc
from dash.dependencies import Input, Output #de dash.dependencies se importa input y output
import math #se importa math
import pandas as pd
import plotly.tools as tls
import plotly.graph_objs as go
#importa las librerías necesarias

#Se importa frontend
from frontend.main import layout
from frontend.centro.centro import update_granulometria_table
from frontend.centro.centro import update_granulometria_plot
from frontend.centro.centro import generate_granulometria_plot

app=dash.Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])
#crea la variable app y agrega __name__ y los estilos con bootstrap

app.layout = layout #se asigna el layout en la variable layout de app







@app.callback(
    Output('tabla_granulometria', 'data'),
    [Input('tabla_granulometria', 'data'),
     Input('tabla_granulometria', 'columns')]
)

def update_tabla_centro(rows, columns):
    return update_granulometria_table(rows, columns)


@app.callback(
    Output('granulometria_plot', 'figure'),
    [Input('tabla_granulometria', 'data')]
)

def update_grafica_centro(rows):
    return update_granulometria_plot(rows)


if __name__ == '__main__': #si __name__ y __main__ son iguales
    app.run_server(debug=True) #Ejecuta la app