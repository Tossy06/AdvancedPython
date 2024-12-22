class Estudiante:
    def __init__(self, nombre, edad, grado):
        self.nombre = nombre
        self.edad = edad
        self.grado = grado
    def estudiar(self):
        print(f'El estudiante {self.nombre}, está estudiando ')

nombre = input('Ingrese el nombre del estudiante: ')
edad = int(input('Ingrese la edad del estudiante: '))
grado = int (input('Ingrese el grado del estudiante: '))

estudiante1 = Estudiante(nombre, edad, grado)

print(f"""
        Datos del Estudiante: \n\n
        Nombre : {estudiante1.nombre} \n
        Edad: {estudiante1.edad} \n
        Grado: {estudiante1.grado}
    """)
    
while True:
    estudiar = input("¿Quieres estudiar? (Escribe 'estudiar' para estudiar o 'salir' para salir): ")
    try:
        if (estudiar.lower() == 'estudiar'):
            estudiante1.estudiar()
        elif estudiar.lower() == 'salir':
            print("Saliendo del programa...")
            break
        else:
            print("Comando no reconocido. Escribe 'estudiar' o 'salir'.")
            
    except Exception as e:
        print(f'Hubo un error al digitar: {e}')
