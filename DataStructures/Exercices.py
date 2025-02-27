#Ejercicio 1: Dado un diccionario con nombres y edades, imprime los nombres de las personas mayores de 25 años.

'''
personas = {'Ana': 23, 'Pedro': 29, 'María': 31, 'Luis': 22}

mayor_edad =  [x for x in personas.values()]
print(max(mayor_edad))
# Sin max
mayor_edad = None

for edad in personas.values():
    if mayor_edad == None or edad > mayor_edad:
        mayor_edad = edad
print(mayor_edad)
'''

#Ejercicio 2: Usando comprensión de listas, genera una lista con los cuadrados de los números del 1 al 10.

'''
cuadrados = [x**2 for x in range(1, 11)]
print(cuadrados)
'''

#Ejercicio 3 (Real-World Case):Tienes una lista de ventas de un mes y quieres obtener solo aquellas mayores a $500. Usa comprensión de listas.
ventas = [100, 550, 430, 600, 200, 800]
mayores_ventas = [x for x in ventas if x > 500]
print(mayores_ventas)