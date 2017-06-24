from rest_framework import serializers, viewsets

from ..models.archivo import Archivo

import logging

log = logging.getLogger(__name__)

from ..utils import SetPagination

class ArchivoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Archivo
        #fields = '__all__'


class ArchivoViewSet(viewsets.ModelViewSet):
    queryset = Archivo.objects.all()
    serializer_class = ArchivoSerializer
    pagination_class = SetPagination