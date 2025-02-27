tupla = (1, 2, 3, 4, 2)

#Se puede recorrer igualq que una lista para obtener sus valores
'''
for i in tupla:
    print(i)
'''
#Sus indices tambien se recorren igual que una lista 
'''
for i in range(len(tupla)):
    print(i)
'''

#Y los indices y valores tambien se recorren al tiempo de la misma forma
'''
for index, valor in enumerate(tupla):
    print(f'Indice: {index}, Valor: {valor}')
'''

#Como las tuplas son inmutables no sepueden agregar ni modificar los datos
# Podemos acceder a sus elemetos por sus inidces y la manera de instanciarlo es con []
print(tupla[0])

#Metodos utiles
print(tupla.count(2)) #El metodo count sirve para saber cuantas veces se repite un elemento en la tupla en este caso el 2
print(tupla.index(4)) # El metodo index sirve para saber el indice de un elemento

