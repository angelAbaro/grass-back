from uuid import uuid4
from django.db import models


class Implemento(models.Model):


    id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    nombre = models.CharField(max_length=100)
    despcripcion = models.IntegerField()
    logo = models.ImageField(verbose_name='Imagen', null=True, upload_to='images/')
    estado = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True,null=True,blank=True)
    updated_at = models.DateTimeField(auto_now=True,null=True,blank=True)



    class Meta:
        verbose_name = "Implemento"
        verbose_name_plural = "Implementos"


    def __str__(self):
        return self.nombre
