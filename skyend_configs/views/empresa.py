from rest_framework import serializers, viewsets

from ..models.empresa import Empresa
from ..utils import SetPagination
import logging
from django.db.models import Q
from operator import __or__ as OR





class EmpresaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Empresa
        #fields = '__all__'


class EmpresaViewSet(viewsets.ModelViewSet):
    queryset = Empresa.objects.all()
    serializer_class = EmpresaSerializer
    pagination_class = SetPagination

    def get_queryset(self):
        query = self.request.query_params.get('query', '')
        queryall = (Q(razon_social__icontains=query),
                    Q(ruc__icontains=query))
        queryset = self.queryset.filter(reduce(OR, queryall))
        return queryset
