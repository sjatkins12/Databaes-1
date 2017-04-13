from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User

from account.models import UserProfile
from .models import ShippingAddress, Report, Subscription, Discussion


# Register your models here.

class UserProfileInline(admin.StackedInline):
    model = UserProfile
    can_delete = False
    verbose_name_plural = 'UserProfile'
    fk_name = 'user'


class CustomUserAdmin(UserAdmin):
    inlines = (UserProfileInline,)
    list_display = ('username', 'email', 'first_name', 'last_name', 'is_staff', 'address')
    list_select_related = ('userprofile',)

    def address(self, instance):
        return instance.userprofile.address

    address.short_description = 'Address'

    def get_inline_instances(self, request, obj=None):
        if not obj:
            return list()
        return super(CustomUserAdmin, self).get_inline_instances(request, obj)


admin.site.unregister(User)
admin.site.register(User, CustomUserAdmin)

admin.site.register(ShippingAddress)
admin.site.register(Report)
admin.site.register(Subscription)
admin.site.register(Discussion)
