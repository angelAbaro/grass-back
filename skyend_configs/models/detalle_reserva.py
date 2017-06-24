from uuid import uuid4
from django.db import models
from catalogo import Catalogo
from reserva import Reserva

class DetalleReserva(models.Model):


    id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    codigo_reserva = models.CharField(max_length=10)
    costo=models.FloatField()
    catalogo=models.ForeignKey(Catalogo)
    reserva = models.ForeignKey(Reserva)
    fecha_inicio=models.DateTimeField()
    fecha_fin = models.DateTimeField()
    created_at = models.DateTimeField(auto_now_add=True,null=True,blank=True)
    updated_at = models.DateTimeField(auto_now=True,null=True,blank=True)


    class Meta:
        verbose_name = "DetalleReserva"
        verbose_name_plural = "DetalleReservas"


    def __str__(self):
        return self.codigo_reserva
