from django.utils.translation import gettext_lazy as _
from django.db.models import TextChoices


class RentStatus(TextChoices):
    CREATED = 'created', _('Created')
    WAITING_DROPOFF = 'waiting_dropoff', _('Waiting for Dropoff')
    WAITING_PICKUP = 'waiting_pickup', _('Waiting for Pickup')
    DELIVERED = 'delivered', _('Delivered')


class RentSize(TextChoices):
    XS = 'xs', _('Extra Small')
    S = 's', _('Small')
    M = 'm', _('Medium')
    L = 'l', _('Large')
    XL = 'xl', _('Extra Large')


class LockerStatus(TextChoices):
    OPEN = 'open', _('Open')
    CLOSED = 'closed', _('Closed')
