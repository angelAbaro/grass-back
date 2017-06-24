from uuid import uuid4
from django.db import models
from.tipo_cancha import TipoCancha


class Cancha(models.Model):
    ESTADO_CHOICES = (
        (u'0', u'libre'),
        (u'1', u'Reservado'),
        (u'2', u'Ocupado'),

    )

    id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    nombre = models.CharField(max_length=100)
    precio = models.IntegerField()
    descripcion = models.TextField()
    estado_reserva = models.CharField(choices=ESTADO_CHOICES,max_length=1,default=0)
    tipo_cancha=models.ForeignKey(TipoCancha)
    estado=models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True,null=True,blank=True)
    updated_at = models.DateTimeField(auto_now=True,null=True,blank=True)

    class Meta:
        verbose_name = "Cancha"
        verbose_name_plural = "Canchas"


    def __str__(self):
        return self.nombre
