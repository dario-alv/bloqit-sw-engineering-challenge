import logging

from django.contrib.auth.models import AbstractUser, BaseUserManager
from django.contrib.auth.password_validation import validate_password
from django.db.models import (Model, CharField, BooleanField, IntegerField, UUIDField,
                              ForeignKey, CASCADE, Index)
from django.utils.translation import gettext_lazy as _
from rest_framework.authtoken.models import Token
from uuid import uuid4

from backend.enums import LockerStatus, RentSize, RentStatus


logger = logging.getLogger(__name__)


class BloqitUserManager(BaseUserManager):

    def create_user(self, username, password=None, **kwargs):
        """
        Creates a normal user with only the username and password.
        :param username: The user's username
        :param password: The user's password
        :return: BloqitUser instance
        """
        user_instance = self.model(username=username, **kwargs)
        # Dev note: not doing password validation here.
        # Doing it on the api instead so that I can throw a drf exception directly if it fails.
        user_instance.set_password(password)
        user_instance.save()
        logger.info(f'User {user_instance} successfully created.')
        return user_instance

    def create_superuser(self, username, password=None, **kwargs):
        """
        Creates a superuser with only the username and password.
        :param username: The superuser's username
        :param password: The superuser's password
        :return: BloqitUser instance
        """
        validate_password(password)
        return self.create_user(username, password, is_staff = True, is_superuser=True, **kwargs)
    

class BloqitUser(AbstractUser):
    
    # Dev note: Decided to override Django's user model to create our own simplified custom user.
    # Since the code challenge doesn't really account for user authentication, I made it as simple as can be.
    # Only a username and password is required.
    # I can safely disregard the other fields that come with the default user model.

    objects = BloqitUserManager()

    # Fields not required for our custom user model.
    email = None
    first_name = None
    last_name = None

    # Overrides the default django user ID to also use UUID's instead
    id = UUIDField(primary_key=True, auto_created=True, default=uuid4, editable=False)

    EMAIL_FIELD = None
    # USERNAME_FIELD = 'username'  # Dev note: already the default
    REQUIRED_FIELDS = []           # Dev note: no required fields since USERNAME_FIELD is default included

    def get_full_name(self) -> str:
        """Overrides the base `get_full_name` to return the username."""
        return f'{self.username}'

    def get_short_name(self) -> str:
        return self.get_full_name()
    
    @property
    def token(self) -> str:
        """Returns a user bearer token."""
        logger.info(f'Generating a token for user {self.id}')
        token, created = Token.objects.get_or_create(user=self)  # only 1 token per user at a time
        return str(token)

    def revoke_token(self) -> None:
        """Revoke the user bearer token."""
        Token.objects.filter(user=self).delete()

    class Meta:
        verbose_name = _('User')
        verbose_name_plural = _('Users')

    def __str__(self):
        return self.get_short_name()


class Bloq(Model):

    id = UUIDField(primary_key=True, auto_created=True, default=uuid4, editable=False)
    title = CharField(max_length=120)
    address = CharField(max_length=200)

    def __str__(self):
        return f'{self.id}'


class Locker(Model):

    id = UUIDField(primary_key=True, auto_created=True, default=uuid4, editable=False)
    bloqId = ForeignKey(Bloq, on_delete=CASCADE)
    status = CharField(max_length=12, choices=LockerStatus.choices)
    isOccupied = BooleanField(default=False)

    def __str__(self):
        return f'{self.id}'
    

class Rent(Model):

    id = UUIDField(primary_key=True, auto_created=True, default=uuid4, editable=False)
    lockerId = ForeignKey(Locker, on_delete=CASCADE)
    weight = IntegerField(default=0)
    size = CharField(max_length=3, choices=RentSize.choices)
    status = CharField(max_length=18, choices=RentStatus.choices)

    def __str__(self):
        return f'{self.id}'
