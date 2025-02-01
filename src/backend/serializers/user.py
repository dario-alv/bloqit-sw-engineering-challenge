import logging

from django.contrib.auth import get_user_model, authenticate, login
from django.contrib.auth.password_validation import validate_password
from rest_framework.serializers import ModelSerializer, CharField
from rest_framework.exceptions import PermissionDenied, AuthenticationFailed

from backend.models import BloqitUser

logger = logging.getLogger(__name__)
user_model = get_user_model()  # Documentation refers this as the preferred way to import the user model.


class UserRegistrationSerializer(ModelSerializer):
    
    class Meta:
        model = user_model
        fields = ['id', 'username', 'password', 'date_joined']
        read_only_fields =  ['id', 'date_joined']
        extra_kwargs = {'password': {'write_only': True}}

    # Dev note: no need to add a unique validator for the username.
    # Drf already identifies the field as unique and validates it accordingly

    def validate_password(self, password):
        try:
            validate_password(password)
        except Exception as e:
            # Dev note: I would normally catch the specific exceptions but there are 4 default validators, 
            #   each with their own exceptions. 
            # Doing extensive password validation takes some time and is also out of scope.
            # I would also not return the exception message to the user like this. 
            raise PermissionDenied(f'Password does not meet requirements: {e}.')
        return password

    def create(self, validated_data):
        username = validated_data.get('username')
        logger.debug(f'Creating a new user with username: {username}')
        return BloqitUser.objects.create_user(**validated_data)


class LoginSerializer(ModelSerializer):

    username = CharField(write_only=True)

    class Meta:
        model = user_model
        fields = ['id', 'username', 'password', 'token']
        read_only_fields =  ['id', 'token']
        extra_kwargs = {'password': {'write_only': True}}
        
    def create(self, validated_data):
        
        username, password = validated_data.get('username'), validated_data.get('password')
        
        if authenticated_account := authenticate(username=username, password=password):  # returns None if not authenticated
            login(self.context['request'], authenticated_account)
            logger.info(f'User login {authenticated_account.id}')
            return authenticated_account

        raise AuthenticationFailed
