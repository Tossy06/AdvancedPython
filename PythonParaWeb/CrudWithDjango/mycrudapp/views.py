from django.shortcuts import render, redirect
from .models import Users
from django.contrib import messages 

# Create your views here.

def register(request):
    if request.method == 'POST':
        user_name = request.POST.get('user_name')
        email = request.POST.get('email')
        password = request.POST.get('password')

        # Guardar datos en la base de datos

        try:
            new_user = Users(user_name = user_name, email = email, password = password)
            new_user.save()
            messages.success(request, 'Usuario registrado con éxito.')
            return redirect('register-login')
        
        except Exception as e:
            messages.error(request, f'Ocurrió un error: {e}')
            return redirect('register-login')
    else:
        return render(request, 'register.html')
    
def home(request):
    return render(request, 'home.html')