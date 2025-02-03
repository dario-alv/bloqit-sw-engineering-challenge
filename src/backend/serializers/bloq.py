import logging

from rest_framework.serializers import ModelSerializer
from backend.models import Bloq

logger = logging.getLogger(__name__)


class BloqSerializer(ModelSerializer):
    
    class Meta:
        model = Bloq
        fields = ['id', 'title', 'address']
        read_only_fields =  ['id']
