import logging

from rest_framework.serializers import ModelSerializer
from backend.models import Locker

logger = logging.getLogger(__name__)


class LockerSerializer(ModelSerializer):
    
    class Meta:
        model = Locker
        fields = ['id', 'bloqId', 'status', 'isOccupied']
        read_only_fields =  ['id']


class EditLockerSerializer(ModelSerializer):
    
    class Meta:
        model = Locker
        fields = ['id', 'bloqId', 'status', 'isOccupied']
        read_only_fields =  ['id', 'bloqId']
