from django.urls import path
from . import views

urlpatterns = [
    # Agrega aquí las rutas de tu app
    path('home/', views.home, name='home'),
]