from rest_framework import serializers, viewsets

from ..models.cancha import Cancha

import logging

log = logging.getLogger(__name__)



class CanchaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cancha
        #fields = '__all__'

from ..utils import SetPagination
class CanchaViewSet(viewsets.ModelViewSet):
    queryset = Cancha.objects.all()
    serializer_class = CanchaSerializer
    pagination_class = SetPagination