# importan las librerias correspondientes
import pandas as pd
from operator import ipow
from matplotlib import axes
import matplotlib.pyplot as plt
import numpy as np

# Determinar la granulomeria como un diccionario de python
# Ingresar la información de la denominación de cada tamiz

def pesoTotal(tamiz_1_1d2, tamiz_1, tamiz_3d4, tamiz_3d8, tamiz_N4, tamiz_N10, tamiz_N20, tamiz_N40, tamiz_N60, tamiz_N100, tamiz_N200):
    # Determinar la granulomeria como un diccionario de python
    # Ingresar la información de la denominación de cada tamiz
    Denominación = pd.Series([
    "1 1/2",
    "1",
    "3/4",
    "3/8",
    "No.4",
    "No.10",
    "No.20",
    "No.40",
    "No.60",
    "No.100",
    "No.200"
    ])

    # Ingresar la información del tamaño de cada tamiz en mm
    Tamiz = pd.Series([
        37.5,  #Tamiz  1 1/2"
        25,    #Tamiz  1"
        19,    #Tamiz  3/4"
        9.5,   #Tamiz  3/8"
        4.75,  #Tamiz  No.4"
        2,     #Tamiz  No.10"
        0.850, #Tamiz  No.20"
        0.425, #Tamiz  No.40"
        0.250, #Tamiz  No.60"
        0.150, #Tamiz  No.100"
        0.075, #Tamiz  No.200"
        ])
    
    # Ingresar la información de la cantidad de muestra que pasa por cada uno de los tamices en gramos
    Pasa = pd.Series([
      tamiz_1_1d2,  #Material pasa Tamiz  1 1/2"
      tamiz_1,  #Material pasa Tamiz  1"
      tamiz_3d4,  #Material pasa Tamiz  3/4"
      tamiz_3d8,   #Material pasa Tamiz  3/8"
      tamiz_N4,   #Material pasa Tamiz  No.4"
      tamiz_N10,   #Material pasa Tamiz  No.10"
      tamiz_N20,   #Material pasa Tamiz  No.20"
      tamiz_N40,   #Material pasa Tamiz  No.40"
      tamiz_N60,   #Material pasa Tamiz  No.60"
      tamiz_N100,   #Material pasa Tamiz  No.100"
      tamiz_N200    #Material pasa Tamiz  No.200"
    ])
    
    # Ingresar la información de el limite superior
    LimiteSuperior = pd.Series([
        100,
        100,
        100,
        100,
        80,
        60,
        44,
        31,
        23,
        17,
        10
        ])
    # Ingresar la información del limite inferior
    LimiteInferior = pd.Series([
        100, 
        70,
        60,
        40,
        30,
        21,
        13,
        8,
        5,
        3,
        0
        ])
