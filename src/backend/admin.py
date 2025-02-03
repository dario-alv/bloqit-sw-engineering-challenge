from django.contrib.admin import register, ModelAdmin
from django.contrib.auth.admin import UserAdmin
from backend.models import BloqitUser, Bloq, Locker, Rent


@register(BloqitUser)
class BloqitUserUserAdmin(UserAdmin):
    
    list_display = ['id', 'username', 'is_staff', 'is_superuser', 'last_login', 'date_joined']
    list_filter = ['is_staff', 'is_superuser']
    ordering = ['id']
    search_fields = ['username']

    # Dev note: Normally I would change this admin entry to allow staff users to change their own passwords,
    # but that is out of scope for this challenge.
    # Setup to allow superusers to change the `is_staff` and `is_superuser` fields of other users is also out of scope.

    def get_fieldsets(self, request, obj=None):
        return (
            (None, {
                'fields': ('id', 'username', 'is_staff', 'is_superuser', 'last_login', 'date_joined'),
            }),
        )
 
    def has_view_permission(self, request, obj=None):
        return True

    def has_add_permission(self, request, obj=None):
        return False

    def has_change_permission(self, request, obj=None):
        return False

    def has_delete_permission(self, request, obj=None):
        return True


@register(Bloq)
class BloqAdmin(ModelAdmin):
    
    list_display = ['id', 'title', 'address']
    ordering = ['id']
    search_fields = ['title', 'address']

    readonly_fields = ['id']
    fieldsets = (
        (None, {
            'fields': ('id', 'title', 'address')
        }),
    )

    def has_view_permission(self, request, obj=None):
        return True

    def has_add_permission(self, request, obj=None):
        return True

    def has_change_permission(self, request, obj=None):
        return True

    def has_delete_permission(self, request, obj=None):
        return True


@register(Locker)
class LockerAdmin(ModelAdmin):
    
    list_display = ['id', 'bloqId', 'status', 'isOccupied']
    ordering = ['id']
    search_fields = ['title', 'status']
    list_filter = ['status', 'isOccupied']

    readonly_fields = ['id']
    fieldsets = (
        (None, {
            'fields': ('id', 'bloqId', 'status', 'isOccupied')
        }),
    )

    def has_view_permission(self, request, obj=None):
        return True

    def has_add_permission(self, request, obj=None):
        return True

    def has_change_permission(self, request, obj=None):
        return True

    def has_delete_permission(self, request, obj=None):
        return True


@register(Rent)
class RentAdmin(ModelAdmin):
    
    list_display = ['id', 'lockerId', 'weight', 'size', 'status']
    ordering = ['id']
    list_filter = ['size', 'status']

    fieldsets = (
        (None, {
            'fields': ('id', 'lockerId', 'weight', 'size', 'status')
        }),
    )

    def has_view_permission(self, request, obj=None):
        return True

    def has_add_permission(self, request, obj=None):
        return False

    def has_change_permission(self, request, obj=None):
        return False

    def has_delete_permission(self, request, obj=None):
        return False
