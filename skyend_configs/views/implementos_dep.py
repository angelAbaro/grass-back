from rest_framework import serializers, viewsets

from ..models.implementos_dep import Implemento

import logging

log = logging.getLogger(__name__)


from ..utils import SetPagination

class ImplementoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Implemento
        #fields = '__all__'


class ImplementoViewSet(viewsets.ModelViewSet):
    queryset = Implemento.objects.all()
    serializer_class = ImplementoSerializer
    pagination_class = SetPagination