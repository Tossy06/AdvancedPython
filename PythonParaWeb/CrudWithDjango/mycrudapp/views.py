from django.shortcuts import render, redirect
from .models import Users, Notas
from django.contrib import messages 
from django.contrib.auth.hashers import check_password, make_password

# Create your views here.

def register(request):
    if request.method == 'POST':
        user_name = request.POST.get('user_name')
        email = request.POST.get('email')
        password = request.POST.get('password')

        # Guardar datos en la base de datos

        try:
            encrypted_password = make_password(password)
            new_user = Users(user_name = user_name, email = email, password = encrypted_password)
            new_user.save()
            messages.success(request, 'Usuario registrado con éxito.')
            return redirect('register-login')
        
        except Exception as e:
            messages.error(request, f'Ocurrió un error: {e}')
            return redirect('register-login')
    else:
        return render(request, 'register.html')


def login (request):
    if request.method == 'POST':
        user_name = request.POST.get('user_name')
        password = request.POST.get('password')
        try:
            #Bucar usuario en la base de datos
            user = Users.objects.get(user_name = user_name)

            if check_password(password, user.password):
                messages.success(request, 'Inicio de sesión exitoso')
                return redirect('home')
            else:
                messages.error(request, 'Contraseña incorrecta')
                return redirect('register-login')
        except Users.DoesNotExist:
            #Para cuando el usuario no se encuntra
            messages.error(request, 'El usuario no existe.')
            return redirect('register-login')
    else:
        return render(request, 'register.html')
    
def home(request):
    user_name = request.GET.get('user_name')

    if request.method == 'POST':
        title = request.POST.get('title')
        content = request.POST.get('content')

        try:
            user = Users.objects.get(user_name = user_name)
            new_note = Notas(title = title, content = content, user= user)
            new_note.save()
            messages.success(request, 'Nota agregada con existo')
            print('Nota agregada')
        except Exception as e:
            messages.error(request, f'Error al guardar la nota: {e}')
            print('No se pudo agregar')
        return redirect('notes')

    return render(request, 'home.html', {'user_name': user_name})

def Notes(request):
    return render( request, 'notes.html')
