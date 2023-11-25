from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User


class CustomUserAdmin(UserAdmin):
    model = User
    list_display = ['id', 'username', 'email', 'first_name', 'last_name', 'is_active']
    search_fields = ['username', 'email']


admin.site.register(User, CustomUserAdmin)