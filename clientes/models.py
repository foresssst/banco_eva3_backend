from django.db import models

class Cliente(models.Model):
    cliente_id = models.CharField(max_length=100, unique=True)
    edad = models.IntegerField()
    genero = models.CharField(max_length=10, choices=[('Masculino', 'Masculino'), ('Femenino', 'Femenino')])
    saldo = models.FloatField()
    activo = models.BooleanField()
    nivel_de_satisfaccion = models.IntegerField(choices=[(i, i) for i in range(1, 6)])

    def __str__(self):
        return f"{self.cliente_id} - {self.edad} años"
