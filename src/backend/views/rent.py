import logging

from django.contrib.auth import get_user_model
from rest_framework.generics import (CreateAPIView, ListAPIView, RetrieveUpdateDestroyAPIView)

from backend.models import Rent
from backend.serializers.rent import RentSerializer, UpdateRentSerializer

logger = logging.getLogger(__name__)
user_model = get_user_model()


class CreateRentView(CreateAPIView):
    
    serializer_class = RentSerializer


class ListRentView(ListAPIView):

    serializer_class = RentSerializer
    queryset = Rent.objects.all()


class UpdateRentView(RetrieveUpdateDestroyAPIView):
    
    serializer_class = UpdateRentSerializer
    lookup_url_kwarg = 'id'
    lookup_field = 'id'
    queryset = Rent.objects.all()
