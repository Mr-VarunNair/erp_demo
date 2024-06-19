from django.contrib import admin


# Register your models here.
#from . models import Asset_Login

#admin.site.register(Asset_Login)
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser

class CustomUserAdmin(UserAdmin):
    fieldsets = UserAdmin.fieldsets + (
        (None, {'fields': ('position',)}),
    )

admin.site.register(CustomUser, CustomUserAdmin)