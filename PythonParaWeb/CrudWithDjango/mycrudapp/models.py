from django.db import models
from django.contrib.auth.hashers import make_password

# Create your models here.
class Users(models.Model):
    user_name = models.CharField(max_length=200, unique= True)
    email = models.EmailField(max_length=200, unique = True)
    password = models.CharField(max_length=200)

    def save(self, *args, **kwargs):
        # Hash de la contraseña antes de guardar en la base de datos
        if not self.pk:  # Solo aplica el hash si es un registro nuevo
            self.password = make_password(self.password)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.user_name