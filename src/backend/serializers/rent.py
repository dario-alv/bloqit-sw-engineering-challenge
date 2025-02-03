import logging

from rest_framework.serializers import ModelSerializer
from backend.models import Rent

logger = logging.getLogger(__name__)


class RentSerializer(ModelSerializer):
    
    class Meta:
        model = Rent
        fields = ['id', 'lockerId', 'weight', 'size', 'status']
        read_only_fields =  ['id', 'status']


class UpdateRentSerializer(ModelSerializer):
    
    # Dev note: I could add a validator here that checks that a rent can only be updated to the next
    #   status in the enums. However, it's not clear if this is intended behavior, so I left it out.

    class Meta:
        model = Rent
        fields = ['id', 'lockerId', 'weight', 'size', 'status']
        read_only_fields =  ['id', 'lockerId']
