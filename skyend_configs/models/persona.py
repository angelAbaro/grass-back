from django.db import models

from uuid import uuid4
class Persona(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    nombre = models.CharField(max_length=10, null=True, blank=True)
    apellido_paterno = models.CharField(max_length=60)
    apellido_materno = models.CharField(max_length=60)
    dni = models.IntegerField()
    telefono = models.IntegerField()
    email = models.EmailField()
    estado = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True,null=True,blank=True)
    updated_at = models.DateTimeField(auto_now=True,null=True,blank=True)

    class Meta:
        verbose_name = "Persona"
        verbose_name_plural = "Personas"

    def __str__(self):
        return self.nombre
