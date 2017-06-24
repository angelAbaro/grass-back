from rest_framework import serializers, viewsets

from ..models.reserva import Reserva

import logging




class ReservaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Reserva
        #fields = '__all__'


class ReservaViewSet(viewsets.ModelViewSet):
    queryset = Reserva.objects.all()
    serializer_class = ReservaSerializer
