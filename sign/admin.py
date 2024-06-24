from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser,Asset_login

class CustomUserAdmin(UserAdmin):
    fieldsets = UserAdmin.fieldsets + (
        (None, {'fields': ('position',)}),
    )

admin.site.register(CustomUser, CustomUserAdmin)

class AssetAdmin(admin.ModelAdmin):
    pass
admin.site.register(Asset_login,AssetAdmin)