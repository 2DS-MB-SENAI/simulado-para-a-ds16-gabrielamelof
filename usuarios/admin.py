from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User

# Register your models here.
class UserAdministrador(UserAdmin):
    list_display = ('username', 'telefone',)

    fieldsets = UserAdmin.fieldsets + (
        (None, {'fields': ('telefone',)}),
    )

    add_fieldsets = UserAdmin.add_fieldsets + (
        (None, {'fields': ('telefone',)}),
    )


admin.site.register(User, UserAdministrador)
