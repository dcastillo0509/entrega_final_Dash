import os
os.chdir(os.path.dirname(__file__))

import pandas as pd
import matplotlib.pyplot as plt #importar la librería matplotlib
from scipy.interpolate import interp1d #Importar la librería scipy para poder interpolar
from operator import ipow
from matplotlib import axes
import numpy as np

malla=[ # Para las mallas
    "1 1/2", #Tamiz 11/2"
    "1", #Tamiz 1"
    "3/4", #Tamiz 3/4"
    "3/8", #Tamiz 3/8"
    "No 4", #Tamiz N°4
    "No 10", #Tamiz N°10
    "No 20", #Tamiz N°20
    "No 40", #Tamiz N°40
    "No 60", #Tamiz N°60
    "No 100", #Tamiz N°100
    "No 200", #Tamiz N°200
    "fondo" #Fondo
]

"""Se crea una lista con el nombre de aberturas donde se ingresa la abertura de cada tamiz"""
abertura=[
    37.5, # Para Tamiz 11/2"
    25, #Para Tamiz 1"
    19, #Para Tamiz 3/4"
    9.5, #Para Tamiz 3/8"
    4.75, #Para Tamiz N°4
    2,  #Para Tamiz N°10
    0.85, #Para Tamiz N°20
    0.425, #Para Tamiz N°40
    0.250, #Para Tamiz N°60
    0.15, #Para Tamiz N°100
    0.075, #Para Tamiz N°200
    0 #Fondo
]

retenido=[
    0, # Para Tamiz 11/2"
    0, #Para Tamiz 1"
    130, #Para Tamiz 3/4"
    150, #Para Tamiz 3/8"
    120, #Para Tamiz N°4
    60, #Para Tamiz N°10
    100, #Para Tamiz N°20
    100, #Para Tamiz N°40
    205, #Para Tamiz N°60
    50, #Para Tamiz N°100
    200, #Para Tamiz N°200
    35 #Fondo
]

granulometria= pd.DataFrame({   #Se crea el dataFrame granulometría
    "Malla": malla, #columana malla
    "Abertura": abertura, #columna abertura
    "Retenido": retenido #columna retenido
}) #Se cierra el dataFrame

granulometria["Retenido_acum"]= granulometria["Retenido"].cumsum()
#se crea una columna para retenido acummulado y se aplica cumsum a la columna retenido para hallar su acumulado
granulometria["Pasa"]= granulometria["Retenido"].sum()-granulometria["Retenido_acum"]
#Se crea la columna Pasa y se realiza la resta del total de la muestra menos el retenido acumulado en cada fila
granulometria["Por_Pasa"]= round(granulometria["Pasa"]*100/granulometria["Retenido"].sum(),2)
#Se crea la columna % pasa y se realiza la operació entre la columna pasa por 100 dividido en el total de la muetra

#INTERPOLACIÓN
# Determinar los diametros para los cuales pasa el 10%, 30% y 60% del material
from scipy.interpolate import interp1d
x = granulometria["Por_Pasa"]
y = abertura

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

Pasa_Tamiz_200 = granulometria.loc[granulometria['Malla'] == 'No 200', 'Por_Pasa'].values[0]
Pasa_Tamiz_4 = granulometria.loc[granulometria['Malla'] == 'No 4', 'Por_Pasa'].values[0]

#---------------------------------------------------------------------------------------------------------------------------------------------------------------------

# CLASIFICAIÓN DEL SUELO
print("El TIPO DE SUELO ES = ")

# SUELOS DE PARTICULAS GRUESAS
if Pasa_Tamiz_200 < 50:
 print("Suelo de partículas gruesas")

# ARENAS
 #Si el porcentaje que pasa el tamiz No.4  es mayor o igual al 50% es una arena
 if Pasa_Tamiz_4 >= 50:
   print("Es una arena")

# Según el valor del tamiz No.200 se tienen tres tipos de arena

# Arena Limpias 
   if Pasa_Tamiz_200 < 5:
    print("Es una arena limpia")
    if Cu >= 6 and 1<= Cc <= 3:
       print("Es una arena bien gradada (SW)")
    if Cu < 6 and 1 > Cc > 3:
       print("Es una arena mal gradada (SP)")

# Arenas con finos
   elif Pasa_Tamiz_200 > 12:
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
   if Pasa_Tamiz_200 > 12:
    print("Es una grava con finos")
    if indicePlasticidad < 4:  #significa que está debajo de la línea A
     print("Es una grava limosa (GM) Verificar en la carta de plasticidad")
    if indicePlasticidad > 7: #significa que está arriba de la línea A
     print("Es una grava Arcillosa (GC) Verificar en la carta de plasticidad")
    
# Gravas limpias
   elif Pasa_Tamiz_200 < 5:
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
 if limliquido > 50:
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

if Pasa_Tamiz_200>= 5:

  # variable que se usa para  añadir texto a la grafica
  ax = plt.axes() 
  # variable que se usa para  añadir texto a la grafica
  # Valores que tomará en x la gráfica para la línea A
  lineaAx = np.linspace(0,100,10)
  # Valores que tomará en y la gráfica para la línea A
  lineaAy=[0.73*(i-20) for i in lineaAx ] 
  # Valores que tomará en x la gráfica para la línea B
  lineaBx = np.linspace(0,100,10)
  # Valores que tomará en y la gráfica para la línea B
  lineaBy=[0.9*(i-8) for i in lineaAx ] 
  # Valores que tomara en x para limitar la linea cuando y=4
  lineaCx = np.array([((4+8*0.9)/0.9),((4+20*0.73)/0.73)])  
  lineaCy = [ 4 for i in lineaCx ]
  # Valores que tomara en x para limitar la linea cuando y=7
  lineaDx = np.array([((7+8*0.9)/0.9),((7+20*0.73)/0.73)])  
  lineaDy = [ 7 for i in lineaCx ]
  lineaEy = np.linspace(0,100,10) 
  lineaEx = [ 50 for i in lineaEy ]
  
  plt.title("CARTA DE PLASTICIDAD",fontsize=18)
  # se ingresa las diferentes rectas que clasifican el suelo en la carta de plasticidad

  plt.plot(lineaAx,lineaAy, label = "Linea A",  color = "black") 
  plt.text(82, 49, 'Línea A',size = 12, rotation = 35)
  plt.plot(lineaBx, lineaBy, label = "Linea B", linestyle = '--', color = "black")
  plt.text(70, 60, 'Línea U',size = 12, rotation = 35)
  plt.plot(lineaCx, lineaCy,color = "black",linestyle = '--')
  plt.plot(lineaDx, lineaDy, linestyle = '--', color = "black" )
  

  plt.plot(lineaEx,lineaEy, color = "black")
  plt.grid(color = 'black', linewidth = 0.7)

  # Comandos que funcionan para añadirle color a la grafica entre las líneas
  plt.fill_between(lineaBx, lineaAy, lineaBy, color='peachpuff',alpha = 1.0)
  plt.fill_between(lineaCx, lineaCy, lineaDy, color='red', alpha = 0.2)
  plt.fill_between(lineaBx, lineaAy, color='cyan', alpha = 0.2)
  
  # Se configura el límite horizontal
  plt.xlim(0, 100)       
  # Se configura el límite vertical 
  plt.ylim(0, 70)            
  
  # Se usa el siguiente comando para añadirle el texto a la gráfica
  ax.text(63,43, "CH U OH", style ="normal",fontsize=8,
          bbox={"facecolor": "white", "alpha": 0.4, "pad":2})
  ax.text(63,23, "MH U OH", style ="normal",fontsize=8,
          bbox={"facecolor": "white", "alpha": 0.4, "pad":2})
  ax.text(23,23, "CL U OL", style ="normal",fontsize=8,
          bbox={"facecolor": "white", "alpha": 0.4, "pad":2})
  ax.text(35,5, "ML U OL", style ="normal",fontsize=8,
          bbox={"facecolor": "white", "alpha": 0.4, "pad":2})
  ax.text(4,7, "CL U ML", style ="normal",fontsize=8,
          bbox={"facecolor": "none", "alpha": 0.4, "pad":2})
  
  # Se añade el nombre de los ejes
  plt.scatter(limliquido, indicePlasticidad, alpha = 1, color = "black")
  plt.xlabel("Límite líquido ",fontsize=14)
  plt.ylabel("Indice de plasticidad",fontsize=14)
  
  plt.show() 

