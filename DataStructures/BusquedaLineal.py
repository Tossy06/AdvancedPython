
lista =[1,2,3,5,5,5,6,7,10,15,20,28,5]

def linear_search(A,x):
    for i, value in enumerate(A):
        if value == x:
            return f'El valor {x}, se encontro en la posición {i} de la lista'
    return f'El valor {x} no se encontró en la lista'

'''
print(linear_search(lista, 5)
'''

#Ahora cuantas veces aparece el valor
def linear_search_count(A,x):
    count = 0
    for value in (A):
        if value == x:
            count +=1
    return f'El valor {x} aparece {count} veces en la lista'

#print(linear_search_count(lista, 5))

def linear_search_last_item(A,x):
    pos = -1
    for i, value in enumerate(A):
        if value == x:
            pos = i
    if pos == -1:
        return f'El valor {x} no se encontró en la lista'
    return f'La última posición en la que se encontró el elemento es: {pos}'
#print(linear_search_last_item(lista,5))

#Traer todas las posiciones donde aparecio el elemento en un diccionario con la posición y el valñor
def linear_search_all_items(A,x):
    pos = {}
    
    for i, value in enumerate(A):
        if value == x:
            pos[i] = value
    return pos if pos else f'El valor {x} no se encontró en la lista'
print(linear_search_all_items(lista,5))

