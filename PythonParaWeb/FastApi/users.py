from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

#Entidad user
class User(BaseModel):
    user_id : int
    name : str
    surname: str
    age: int

# Lista simulada de usuarios (base de datos simulada)
users_db = [
    User(user_id=1, name='David', surname='Gómez', age=18),
    User(user_id=2, name='Laura', surname='Martínez', age=25),
    User(user_id=3, name='Carlos', surname='Pérez', age=30),
]


#Get wiht id

@app.get('/usersjson/{user_id}')
async def users_with_id(user_id: int):
    for user in users_db:
        if user.user_id == user_id:
            return user
    return({'error': 'El usuario no existe'})

#Post

@app.post('/usersjson/')
async def new_user(new_user: User):
    
    user_data = {
        'user_id': new_user.user_id,
        'name': new_user.name,
        'surname': new_user.surname,
        'age': new_user.age
    }
    users_db.append(user_data)
    return {"message": "Usuario creado con éxito", "user": user_data}