from django.contrib import admin
from django.contrib import auth

from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.utils.html import mark_safe
from chotot.models import *


class UserAdmin(BaseUserAdmin):
    list_display = ('id','email', 'username',)
    search_fields = ('email', 'username',)

    fieldsets = BaseUserAdmin.fieldsets
    fieldsets[0][1]['fields'] = fieldsets[0][1]['fields'] + (
        'avatar',
    )

    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email','username', 'password1', 'password2','avatar')}
        ),
    )
admin.site.register(User,UserAdmin)
admin.site.unregister(auth.models.Group)