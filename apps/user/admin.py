from django.contrib import admin

# Register your models here.
from apps.user.models import *


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = (
        'id', 'username', 'first_name', 'last_name', 'email', 'is_active', 'password', 'date_joined', 'last_login')
    list_per_page = 50
    ordering = ('id',)
    list_display_links = ('id', 'username')
