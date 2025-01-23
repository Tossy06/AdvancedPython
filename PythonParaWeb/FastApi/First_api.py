from fastapi import FastAPI

app = FastAPI()

#Datos

usuarios = [{'id': 1, 'nombre': 'David' }, {'id':2, 'nombre':'Alejandra'}]

@app.get('/usuarios')
async def obtener_usuarios():
    return usuarios

#Obtener por ususarios
@app.get('/usuarios/{usuario_id}')
async def obetener_usuarios(usuario_id : int):
    for usuario in usuarios:
        if usuario['id'] == usuario_id:
            return usuario
    return {"error": "Usuario no encontrado"}