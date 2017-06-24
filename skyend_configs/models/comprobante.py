from uuid import uuid4
from django.db import models
from detalle_reserva import DetalleReserva


class Comprobante(models.Model):


    id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    detalle_reserva = models.ForeignKey(DetalleReserva)
    created_at = models.DateTimeField(auto_now_add=True,null=True,blank=True)
    updated_at = models.DateTimeField(auto_now=True,null=True,blank=True)


    class Meta:
        verbose_name = "Comprobante"
        verbose_name_plural = "Comprobantes"


    def __str__(self):
        return self.id
