from django.db import models

class Producto(models.Model):
    nombre_producto = models.CharField(max_length=50)
    precio = models.CharField(max_length=11)
    ver_mas = models.TextField()
    fecha = models.DateField(null=True, blank=True)  # Permitir valores nulos y en blanco
    imagen = models.ImageField(upload_to='productos/')

    def __str__(self):
        return self.nombre_producto
