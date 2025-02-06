import seaborn as sns
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import math

df = sns.load_dataset('tips')
print(df.head(5))

#Media de propinas
def media(datos):
    media = sum(datos)/len(datos)
    return media
media_tip = media(df['tip'])
print(f'La media es: {media_tip}')
'''
tip =df['tip']
media = tip.mean()
print(media)
'''

#Modo
def moda (dato):
    contador = {}
    for clave in dato['tip']:
        if clave in contador:
            contador[clave] += 1
        else:
            contador[clave] = 1
    return(max(contador, key=contador.get))

moda_tip = moda(df)
print(f'La moda es: {moda_tip}')

'''
moda_data = df['tip']
moda_fuction = moda_data.mode()
print(moda_fuction)
'''

#Mediana
def mediana (dato):
    sorted_data = sorted(dato)
    n = len(sorted_data)
    if n % 2 == 0:
        mid1 = n //2 - 1
        mid2 = n //2
        mediana = (sorted_data[mid1]+ sorted_data[mid2])/2
    else:
        mid = n //2
        mediana = sorted_data[mid]
    return mediana

mediana_tip = mediana(df['tip'])
print(f'La mediana es: {mediana_tip}')

'''
median_df = df['tip']
median_fuction = median_df.median()
print(median_fuction)
'''

# varianza 
def varianza (dato):
    dato_media = media(dato)
    suma_cuadrados = sum((i-dato_media)**2 for i in dato)
    var = suma_cuadrados / len(dato)
    return var

resultado = varianza(df['tip'])
print(f'La varianza es: {resultado}')

'''
varia_data = df['tip']
resultado_fuction = varia_data.var()
print(resultado_fuction)
'''

def desviacion(dato):
    dato_varianza = varianza(dato)
    desviacion_estandar = math.sqrt(dato_varianza)
    return desviacion_estandar
resultado_des = desviacion(df['tip'])
print(f'La desviación estadar es: {resultado_des}')

'''
desviacion_dato = df['tip']
resultado_fuction = desviacion_dato.std()
print(resultado_fuction)
'''

#Grafica histograma

plt.hist(df['tip'], bins=15, edgecolor = 'black', align='mid')
plt.xlabel('Monto de propina')
plt.ylabel('Frecuencia')
plt.title('Distribucuion de las propinas')
plt.show()

    