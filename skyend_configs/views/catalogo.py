from rest_framework import serializers, viewsets

from ..models.catalogo import Catalogo

import logging

log = logging.getLogger(__name__)



from ..utils import SetPagination
class CatalogoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Catalogo
        #fields = '__all__'


class CatalogoViewSet(viewsets.ModelViewSet):
    queryset = Catalogo.objects.all()
    serializer_class = CatalogoSerializer
    pagination_class = SetPagination