from django.db import models

class Producto(models.Model):
    nombre_producto = models.CharField(max_length=50)
    precio = models.CharField(max_length=11)

    def __str__(self):
        return self.nombre_producto
