from django.db import models

# Create your models here.
class Users(models.Model):
    user_name = models.CharField(max_length=200, unique= True)
    email = models.EmailField(max_length=200, unique = True)
    password = models.CharField(max_length=200)

    def __str__(self):
        return self.user_name
