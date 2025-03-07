
#Suma sin numpy y usando compresión de listas
v_1 = [1,2,3]
v_2 = [4,5,6]
suma = [v_1[i] + v_2[i] for i in range(len(v_1))]
print(suma) 

#Producto Escalar
producto_ecalar = sum(v_1[i] * v_2[i] for i in range(len(v_1)))
print(producto_ecalar)