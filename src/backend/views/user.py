import logging

from django.contrib.auth import logout
from rest_framework.generics import CreateAPIView
from rest_framework.response import Response
from rest_framework.status import HTTP_204_NO_CONTENT 
from rest_framework.permissions import AllowAny

from backend.serializers.user import UserRegistrationSerializer, LoginSerializer

logger = logging.getLogger(__name__)


class UserRegistrationView(CreateAPIView):
    
    authentication_classes = ()
    permission_classes = (AllowAny,)
    serializer_class = UserRegistrationSerializer


class LoginView(CreateAPIView):

    authentication_classes = ()
    permission_classes = (AllowAny,)
    serializer_class = LoginSerializer


class LogoutView(CreateAPIView):

    def post(self, request, *args, **kwargs):
        request.user.revoke_token()
        logout(request)
        logger.info(f'User {request.user.id} logged out.')
        return Response({}, status=HTTP_204_NO_CONTENT)
