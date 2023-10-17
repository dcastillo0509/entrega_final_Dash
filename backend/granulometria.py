import os
os.chdir(os.path.dirname(__file__))

import pandas as pd
import matplotlib.pyplot as plt #importar la librería matplotlib
from scipy.interpolate import interp1d #Importar la librería scipy para poder interpolar


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
x = granulometria["Porcentaje Pasa"]
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