a = [[1,2], 
     [3,4],
]
b = [
    [5,6],
    [7,8]
]

'''
resultado = [[0 for _ in range(2)] for _ in range(2)]

for i in range(2):
    for j in range(2):
        resultado[i][j] = a[i][j] * b[i][j]

for fila in resultado:
    print(fila)

'''
'''
#Multiplicación de matrices
def multiplicar_matrices(A, B):

    filas_A = len(A)
    columnas_A = len(A[0])

    filas_B = len(B)
    columnas_B = len(A[0])
    # Verificamos si se pueden multiplicar
    if columnas_A != filas_B:
        raise ValueError("Las matrices no se pueden multiplicar (columnas de A deben ser iguales a filas de B)")
    
    matriz_c = [[0 for _ in range(columnas_B)] for _ in range(filas_A)]
    
    for i in range(filas_A):
        for j in range(columnas_B):
            #Aqui hacemos otro for para acceder a los elementos
            for k in range (columnas_A):
                matriz_c[i][j] += A[i][k] * B[k][j]

    return matriz_c

resultado = multiplicar_matrices(a, b)

for fila in resultado:
    print(fila)
'''
#Transformación lineal

def transformación_linea(A, x):
    return [sum(A[i][j] * x[j] for j in range(len(x))) for i in range(len(A))]

A = [[2, 0], 
     [0, 3]]

x = [1, 2]

resultado = transformación_linea(A, x)
print(resultado)