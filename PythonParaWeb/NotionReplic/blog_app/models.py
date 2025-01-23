from django.db import models
from usersmanage.models import Users

# Create your models here.
class Blog(models.Model):
    title = models.CharField(max_length=200)
    content = models.CharField(max_length=8000)
    user_name = models.ForeignKey(Users, on_delete= models.CASCADE)
