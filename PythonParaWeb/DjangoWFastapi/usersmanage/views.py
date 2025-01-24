from django.shortcuts import render, redirect
from django.urls import reverse
from django.contrib.auth.hashers import check_password, make_password
from .models import User


# Create your views here.
def register(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        password = request.POST.get('password')
        encrypted_password = make_password(password)

        new_user = User(name = name, email = email, password = encrypted_password)
        new_user.save()
        return redirect(reverse('register'))
    
    else:
        return render(request, 'register.html')
