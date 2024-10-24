from django.db import models

class Fabrica(models.Model):
    nombre = models.CharField(max_length=100)
    pais = models.CharField(max_length=100, null=True, blank=True)

    def __str__(self):
        return self.nombre

class Producto(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField()
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    fabrica = models.ForeignKey(Fabrica, on_delete=models.CASCADE, null=True, blank=True)
    f_vencimiento = models.DateField(null=True, blank=True)

    def __str__(self):
        return self.nombre