import pandas as pd
import re

# Leer el archivo de texto de WhatsApp
with open(r"Nombre de chat", 'r', encoding='utf-8') as file:
    lines = file.readlines()
# Crear un DataFrame vacío para almacenar los datos
messages = []

# Procesar cada línea del chat
for line in lines:
    # Suponiendo que el formato es "fecha - nombre: mensaje"
    if '-' in line:
        part = line.split('-', 1)
        data_time = part[0]
        message = part[1].strip()
        if ':' in message:
            sender, content = message.split(':', 1)
            messages.append([data_time, sender, content])
df = pd.DataFrame(messages, columns=['Fecha', 'Remitente', 'Mensaje'])
print(df.head(5))

conteo =df['Mensaje'].str.count(r'\b\W*amor\W*\b', flags=re.IGNORECASE).sum()
print(conteo)
print(df.shape)



