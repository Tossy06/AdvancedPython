from sklearn.datasets import fetch_california_housing
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

data = fetch_california_housing(as_frame=True)
df = pd.DataFrame(data.data, columns=data.feature_names)
df["target"] = data.target  # Agregar la variable objetivo (precio de vivienda)

#Medidas de tendencia
media = np.mean(df["target"])
mediana = np.median(df["target"])
moda = df["target"].mode()[0]

print(f'Media de precios: {media} ')
print(f'Mediana de precios: {mediana} ')
print(f'Moda de precios: {moda} ')

#Medidas de tendencia hechar por codigo

#Media

def media(datos):
    suma = sum(datos)/ len(datos)
    return suma
print(media(df["target"]))

#Mediana
precios_ordenados = sorted(df["target"])
mediana = (precios_ordenados[10320]+ precios_ordenados[10321])/2
print(mediana)

#Moda
contador = {}
for clave in df["target"]:
    if clave in contador:
        contador[clave] +=1
    else:
        contador[clave] = 1
print(max(contador, key=contador.get))

