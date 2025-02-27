import pandas as pd

lista = [2, 1, 5, 4, 3]

#Las listas se recorren con bucles ccomúnmente el for

'''
for num in lista:
    print(num)
'''
#Aqui estoy recorriendo la lsita, pero no los elementos de esta si no que los indices de la lista
#Range tiene una estructura (inicio:final:paso), aqui estamos pasando solo el final, osea hasta donde se va arecorrer
'''
for i in range (len(lista)):
    print(i)
'''

#Aqui estoy recorriendo la lista por indices, pero ademas traigo el valor del indice de la siguiente form:
#lista[i], que lo que hace es entras al valor del indice que le estoy pasando
'''
for i in range (len(lista)):
    print(f'Indice: {i}, Valor: {lista[i]}')
'''

#Las listas son mutables, por lo que podemos cambiar y modificar los valores de la tabla
#algunos de sus funciones  son: append, insert, remove , pop, sort

'''
#Append se utiliza para añadir un valor al final de la lista y se instancia con ()
lista.append(4)
print(lista)
#Por otro lado insert se utiliza para añadir un valor en una posición en especifico
lista.insert(1,10)
print(lista)
#Remove, se utiliza cuando conozco el valor y quiero elimarlo:
lista.remove(10)
print(lista)
#Pop elimina el ultipmo elemento de la lista
lista.pop()
print(lista)
#Sort organiza los elementos de la tabla
lista.sort()
print('Lista ordenada: ', lista)
#Tambien se puede hacer de forma descendente
lista.sort(reverse=True)
print('Lista ordenada en orden descendente: ',lista)
'''

#Interactuando con datos de pandas
'''
datos = {'Nombre': ['David', 'Aleja', 'Panchito'], 'Edad': [19, 19, 4]}
df = pd.DataFrame(datos)

#En este for estoy recorriendo tanto el indice como los valores del dt en la columna de la edad
for index, edad in enumerate(df['Edad']):
    if edad >= 18: # Condición para saber cuales edades son mayores a 18
        print(df.loc[index, 'Nombre']) # Con la función loc, ingresamos a el indice y al valor de la columan de nombre

#Pero una simplificación del codigo anterior solo con pandas seria algo asi
#Nota: loc tiene la siguiente estructura [fila, columna], la fila puede ser un indice espeficico, rango o condición, y la columna, el nombre de la columna o un rango de nombres
print(df.loc[df['Edad']>=18, ['Nombre', 'Edad']])
'''
#Compresión de listas
cuadrados = []
for x in range (10 + 1):
    cuadrados.append(x**2)
print(cuadrados)
#Pero esto se puede gacer con compresión de listas que es más eficiente
cuadrados_2 = [x**2 for x in range (10 + 1)]
print(cuadrados_2)