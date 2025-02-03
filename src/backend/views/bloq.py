import logging

from django.contrib.auth import get_user_model
from rest_framework.generics import (CreateAPIView, ListAPIView, RetrieveAPIView, RetrieveUpdateDestroyAPIView)
from rest_framework.permissions import IsAdminUser

from backend.models import Bloq
from backend.serializers.bloq import BloqSerializer

logger = logging.getLogger(__name__)
user_model = get_user_model()


class CreateBloqView(CreateAPIView):
    """Staff only"""
    permission_classes = [IsAdminUser]  # Only staff can place a Bloq
    serializer_class = BloqSerializer


class ListBloqView(ListAPIView):
    
    # Dev note: It would be a good idea to add some query param filters here so that this api can
    # be filtered (`address` for example). Out of scope for the challenge.
    
    serializer_class = BloqSerializer
    queryset = Bloq.objects.all()


class RetrieveBloqView(RetrieveAPIView):
    
    serializer_class = BloqSerializer
    lookup_url_kwarg = 'id'
    lookup_field = 'id'
    queryset = Bloq.objects.all()


class EditDeleteBloqView(RetrieveUpdateDestroyAPIView):
    """Staff only"""
    permission_classes = [IsAdminUser]  # Only staff can edit and remove a Bloq
    http_method_names = ['put', 'patch', 'delete']
    serializer_class = BloqSerializer
    lookup_url_kwarg = 'id'
    lookup_field = 'id'
    queryset = Bloq.objects.all()
