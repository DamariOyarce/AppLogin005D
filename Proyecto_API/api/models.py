from django.db import models

# Create your models here.
class Usuario(models.Model):
    nombreusuario=models.CharField(max_length=50)
    email= models.EmailField(max_length=100)
    contraseña = models.CharField(max_length=50)
