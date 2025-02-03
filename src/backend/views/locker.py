import logging

from django.contrib.auth import get_user_model
from rest_framework.generics import (CreateAPIView, ListAPIView, RetrieveUpdateAPIView, DestroyAPIView)
from rest_framework.permissions import IsAdminUser

from backend.models import Locker
from backend.serializers.locker import LockerSerializer, EditLockerSerializer

logger = logging.getLogger(__name__)
user_model = get_user_model()


class CreateLockerView(CreateAPIView):
    """Staff only"""
    permission_classes = [IsAdminUser]      # Only staff can place a Locker
    serializer_class = LockerSerializer


class ListLockerView(ListAPIView):
    
    serializer_class = LockerSerializer
    queryset = Locker.objects.all()


class UpdateLockerView(RetrieveUpdateAPIView):
    
    serializer_class = EditLockerSerializer
    lookup_url_kwarg = 'id'
    lookup_field = 'id'
    queryset = Locker.objects.all()


class DeleteLockerView(DestroyAPIView):
    """Staff only"""
    permission_classes = [IsAdminUser]      # Only staff can remove a Bloq
    serializer_class = LockerSerializer
    lookup_url_kwarg = 'id'
    lookup_field = 'id'
    queryset = Locker.objects.all()
