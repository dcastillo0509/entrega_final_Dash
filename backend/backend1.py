# importan las librerias correspondientes
import pandas as pd
from operator import ipow
from matplotlib import axes
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker
import numpy as np

# Determinar la granulomeria como un diccionario de python
# Ingresar la información de la denominación de cada tamiz

def pesoTotal(tamiz_1_1d2, tamiz_1, tamiz_3d4, tamiz_3d8, tamiz_N4, tamiz_N10, tamiz_N20, tamiz_N40, tamiz_N60, tamiz_N100, tamiz_N200):
    
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
    return Pasa


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
    1150,  #Material pasa Tamiz  1 1/2"
    1150,  #Material pasa Tamiz  1"
    1020,  #Material pasa Tamiz  3/4"
    870,   #Material pasa Tamiz  3/8"
    750,   #Material pasa Tamiz  No.4"
    690,   #Material pasa Tamiz  No.10"
    590,   #Material pasa Tamiz  No.20"
    490,   #Material pasa Tamiz  No.40"
    285,   #Material pasa Tamiz  No.60"
    235,   #Material pasa Tamiz  No.100"
    100    #Material pasa Tamiz  No.200"
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

# Determinar la informacion y los nombres que se van a presentar el la base de datos de Granulometria 
Granulometria = pd. DataFrame({
    "Denominación": Denominación,
    "Tamiz(mm)": Tamiz,
    "Pasa(g)": Pasa,
    "Porcentaje Pasa" : Pasa*100/1150,
    "Limite Superior" : LimiteSuperior,
    "Limite Inferior" : LimiteInferior
})
print(Granulometria)


#CURVA GRANULOMETRICA CON LIMITES
# Establecer cual la información con la que se realizara la grafica
def plot_granulometric_curve(Tamiz, Porcentaje_Pasa, LimiteSuperior, LimiteInferior):
    fig, ax = plt.subplots()
    
    # Configurar la gráfica principal
    ax.plot(Tamiz, Porcentaje_Pasa, color='m', lw=2, linestyle='--', label="Curva Granulométrica")
    
    # Configurar las líneas de límite
    ax.plot(Tamiz, LimiteSuperior, color='yellow', linestyle='-', label="Limite Superior")
    ax.plot(Tamiz, LimiteInferior, color='blue', linestyle='-', label="Limite Inferior")
    
    # Nombrar los ejes
    ax.set_title("Curva Granulométrica", fontsize=15)
    ax.set_xlabel("Tamiz (mm)", fontsize=12)
    ax.set_ylabel("% Pasa", fontsize=12)
    ax.legend(bbox_to_anchor=(1.05, 1.0), loc='upper left')
    
    # Escala logarítmica en el eje x
    ax.set_xscale('log')
    
    # Invertir el eje x
    ax.invert_xaxis()
    
    # Grilla en el eje x (escala logarítmica)
    ax.grid(True, which="minor", linestyle='-')
    
    # Grilla normal en el eje y
    ax.grid(True, which='minor', linestyle='-', label="Granulometría del suelo")
    
    plt.show()

# Llama a la función proporcionando los datos necesarios
plot_granulometric_curve(Tamiz, Granulometria["Porcentaje Pasa"], LimiteSuperior, LimiteInferior)

#---------------------------------------------------------------------------------------------------------------------------------------------------------------
# Ingresar el valor del limite liquido y del inice de plasticidad
limLiquido = 7
print("Limite liquido = ",limLiquido)
indicePlasticidad = 4
print("Indice de plasticidad = ",indicePlasticidad)

#------------------------------------------------------------------------------------------------------------------------------------------------------------------

#INTERPOLACIÓN
# Determinar los diametros para los cuales pasa el 10%, 30% y 60% del material
from scipy.interpolate import interp1d
x = Granulometria["Porcentaje Pasa"]
y = Tamiz

interpolate_x = 10
y_interp =interp1d(x, y )
D10=y_interp(interpolate_x)

interpolate_x = 30
D30=y_interp(interpolate_x)

interpolate_x = 60
D60=y_interp(interpolate_x)

# -------------------------------------------------------------------------------------------------------------------------------------------------------------------
# Coeficiente de uniformidad (Cu)  y Coeficiente de curvatura (Cc)
# Calculamos el valor del Cu y Cc

Cu = D60/D10
print("Cu =",Cu)
Cc = (D30**2)/(D10*D60)
print("Cc =",Cc)

#-------------------------------------------------------------------------------------------------------------------------------------------------------------------
# Determinar los valores para el tamiz No. 200 y No.4, para hacer la clasificaion del suelo
Tamiz_200 = Granulometria["Porcentaje Pasa"][10]
print("Tamiz No.200 =", Tamiz_200)
Tamiz_4 = Granulometria["Porcentaje Pasa"][4]
print("Tamiz No.4 =" , Tamiz_4 )

#---------------------------------------------------------------------------------------------------------------------------------------------------------------------

# CLASIFICAIÓN DEL SUELO
def clasificacion_suelo(Tamiz_200, Tamiz_4, Cu, Cc, indicePlasticidad, limLiquido):
    resultado = "El TIPO DE SUELO ES = "
    
    # SUELOS DE PARTICULAS GRUESAS
if Tamiz_200 < 50:
 print("Suelo de partículas gruesas")

# ARENAS
 #Si el porcentaje que pasa el tamiz No.4  es mayor o igual al 50% es una arena
 if Tamiz_4 >= 50:
   print("Es una arena")

# Según el valor del tamiz No.200 se tienen tres tipos de arena

# Arena Limpias 
   if Tamiz_200 < 5:
    print("Es una arena limpia")
    if Cu >= 6 and 1<= Cc <= 3:
       print("Es una arena bien gradada (SW)")
    if Cu < 6 and 1 > Cc > 3:
       print("Es una arena mal gradada (SP)")

# Arenas con finos
   elif Tamiz_200 > 12:
    print(" Arena con finos")
    if indicePlasticidad < 4: #significa que está debajo de la línea A
      print("Es una arena arcillosa (SC) Verificar en la carta de plasticidad")
    if indicePlasticidad > 7: #significa que está arriba de la línea A
      print("Es una arena limosa (SM) Verificar en la carta de plasticidad")
 
 # Arenas limpias y con finos
   else:
    print("Es una arena limpia y con finos")
#Bien gradada
    if Cu >= 6 and 1 <= Cc <= 3: 
      if indicePlasticidad < 4: #significa que está debajo de la línea A
        print("Es una arena bien gradada con limo (SW-SM) Verificar en la carta de plasticidad")
      if indicePlasticidad > 7: #significa que está arriba de la línea A
        print("Es una arena bien gradada con arcilla (SW-SC) Verificar en la carta de plasticidad")
# Mal gradada
    else: 
      if indicePlasticidad < 4: #significa que está debajo de la línea A
        print("Es una arena mal gradada con limo (SP-SM) Verificar en la carta de plasticidad")
      if indicePlasticidad > 7: #significa que está arriba de la línea A
        print("Es una arena mal gradada con arcilla (SP-SC) Verificar en la carta de plasticidad")
#---------------------------------------------------------------------------------------------------------------------------------------------------------------
# SUELOS DE PARTICULAS GRUESAS
# GRAVAS
 else:
   print("Es una grava")

# Según el valor del tamiz No.200 se tienen tres tipos de grava

# Gravas con finos 
   if Tamiz_200 > 12:
    print("Es una grava con finos")
    if indicePlasticidad < 4:  #significa que está debajo de la línea A
     print("Es una grava limosa (GM) Verificar en la carta de plasticidad")
    if indicePlasticidad > 7: #significa que está arriba de la línea A
     print("Es una grava Arcillosa (GC) Verificar en la carta de plasticidad")
    
# Gravas limpias
   elif Tamiz_200 < 5:
     print("Es una grava limpia")
     if Cu >= 4 and 1 <= Cc <= 3:
      print("Es una Grava bien gradada (GW)")
     if Cu < 4 and 1 > Cc > 3:
      print("Es una Grava mal gradada (GP)")
  
# Gravas limpias y con finos
   else:
     print("Es una grava limpia y con finos")

    # Segun el Cu y el Cc se clasifican las arenas limpias y con finos 

    # Bien gradada
   if Cu >= 4 and 1 <= Cc <= 3:
    if indicePlasticidad < 4: #significa que está debajo de la línea A
     print("Es una grava bien gradada con limo (GW-GM) Verificar en la carta de plasticidad")
    if indicePlasticidad > 7: #significa que está arriba de la línea A
     print("Es una grava bien gradada con arcilla (GW-GC) Verificar en la carta de plasticidad")

    # Mal gradada
   else:
    if indicePlasticidad < 4: #significa que está debajo de la línea A
     print("Es una grava mal gradada con limo (GP-GM) Verificar en la carta de plasticidad")
    if indicePlasticidad > 7: #significa que está arriba de la línea A
     print("Es una grava mal gradada con arcilla (GP-GC) Verificar en la carta de plasticidad")
#-------------------------------------------------------------------------------------------------------------------------------------------------
# SUELOS DE PARTICULAS FINAS
else:
 print("Suelo de partículas finas")
 if limLiquido > 50:
   # Inorgánicos de alta plasticidad
   print("El suelo puede ser una arcilla o un limo de alta plasticidad")
   if indicePlasticidad < 4: #significa que está debajo de la línea A
     print("Es un limo de alta plasticidad (MH) Verificar en la carta de plasticidad")
   if indicePlasticidad > 7: #significa que está arriba de la línea A
     print("Es una arcilla de alta plasticidad (CH) Verificar en la carta de plasticidad")


   # Inorgánicos de baja plasticidad
 else:
  print("El suelo puede ser una arcilla o un limo de baja plasticidad")
  if indicePlasticidad < 4: #significa que está debajo de la línea A
     print("Es un limo de baja plasticidad (ML) Verificar en la carta de plasticidad")
  if indicePlasticidad > 7: #significa que está arriba de la línea A
     print("Es una arcilla de baja plasticidad (CL) Verificar en la carta de plasticidad")



#-----------------------------------------------------------------------------------------------------------------------------------------------------------------
#CARTA DE PLASTICIDAD

# Condicionamos la carta de plasticidad debido a que si es una arena limpia o una grava limpia no se usa la carta de plasticidad
# Determinar cada uno de los parametros que debe llevar la carta de plasticidad  

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