from django.urls import path
from . import views

urlpatterns = [
    path('register-login/', views.register, name='register-login'),
    path('home/', views.home, name='home')
]