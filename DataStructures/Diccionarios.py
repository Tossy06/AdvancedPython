
#Los diccionarios sos estructuras de datos basados en claves y valores
personas = {'Ana': 23, 'Pedro': 29, 'María': 31, 'Luis': 22}

'''

# De esta manera recorremos las claves de un diccionario
for i in personas:
    print(i)

#Y este caso recorre el indice y la clave
for index, clave in enumerate(personas):
    print(f'Indez: {index}, Clave: {clave}')

#Pero el metodo values, se encargara de darnos los valores de la clvaes
for valor in personas.values():
    print(valor)
#Y si quiero recorrer las claves junto a los valores se utiliza item
for clave, valor in personas.items():
    print(f'Clave:{clave}, Valor: {valor}')

#Y si quiero crear una lista solo con los valore sutilizo list comprehesión
#Nota: la Estructura de un list comprehesión es: expresión for el inidice de la expresión in la condición

valores = [valor for valor in personas.values()]
print(f'La lsita de valores es: {valores}')
'''

#Metodos

#De esta forma de agrega un clave junto a su valor
personas['Panchito'] = 4
print(personas)

# Y para elimianr elementos se utiliza el pop
'''
personas.pop('Panchito')
print(personas)
'''
#O
del personas['Panchito']
print(personas)