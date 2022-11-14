from django.db import models

# Create your models here.
class ProductosH(models.Model):
    nombre = models.CharField(max_length=15)
    precio = models.IntegerField()
    imagen = models.ImageField(upload_to="productos", null=True)

class ProductosM(models.Model):
    nombre = models.CharField(max_length=15)
    precio = models.IntegerField()
    imagen = models.ImageField(upload_to="productos", null=True)

class ProductosN(models.Model):
    nombre = models.CharField(max_length=15)
    precio = models.IntegerField()
    imagen = models.ImageField(upload_to="productos", null=True)