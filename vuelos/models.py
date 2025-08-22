from django.db import models

# Create your models here.
class Vuelo(models.Model):
    #defino el tipo de elecciones que puede tener el campo tipo
    TIPO_VUELO = [
        ('nacional', 'Nacional'),
        ('internacional', 'Internacional'),
    ]

    id = models.AutoField(primary_key=True)
    nombre_vuelo = models.CharField(max_length=100, unique=True)
    tipo = models.CharField(max_length=50, choices=TIPO_VUELO)
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    
    #este es solo pa verlo en el admin site
    def __str__(self):
        return f"Vuelo con nombre:::: {self.nombre_vuelo} ({self.tipo})"