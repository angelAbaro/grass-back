from uuid import uuid4
from django.db import models
from .cancha import Cancha
from .implementos_dep import Implemento
from .local import Local

class Catalogo(models.Model):


    id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    cancha =models.ForeignKey(Cancha,null=True,blank=True)
    implemento = models.ForeignKey(Implemento,blank=True,null=True)
    local=models.ForeignKey(Local)
    estado = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True,null=True,blank=True)
    updated_at = models.DateTimeField(auto_now=True,null=True,blank=True)


    class Meta:
        verbose_name = "Catalogo"
        verbose_name_plural = "Catalogos"


    def __str__(self):
        return self.razon_social
