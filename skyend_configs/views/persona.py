from rest_framework import serializers, viewsets

from ..models.persona import Persona

import logging

log = logging.getLogger(__name__)



from ..utils import SetPagination
class PersonaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Persona
        #fields = '__all__'


class PersonaViewSet(viewsets.ModelViewSet):
    queryset = Persona.objects.all()
    serializer_class = PersonaSerializer
    pagination_class = SetPagination
