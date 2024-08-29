# admin.py
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser

class CustomUserAdmin(UserAdmin):
    model = CustomUser
    list_display = ['username', 'email', 'first_name', 'last_name', 'age', 'phone_number', 'is_staff']
    list_filter = ['is_staff', 'is_active', 'age']
    fieldsets = UserAdmin.fieldsets + (
        (None, {'fields': ('age', 'phone_number', 'address')}),
    )
    add_fieldsets = UserAdmin.add_fieldsets + (
        (None, {'fields': ('age', 'phone_number', 'address')}),
    )

admin.site.register(CustomUser, CustomUserAdmin)
