from rest_framework import serializers, viewsets

from ..models.local import Local

import logging

log = logging.getLogger(__name__)



from ..utils import SetPagination
class LocalSerializer(serializers.ModelSerializer):
    class Meta:
        model = Local
        #fields = '__all__'


class LocalViewSet(viewsets.ModelViewSet):
    queryset = Local.objects.all()
    serializer_class = LocalSerializer
    pagination_class = SetPagination

