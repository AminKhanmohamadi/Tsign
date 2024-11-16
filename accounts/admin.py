from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from accounts.forms import CustomUserCreationForm, CustomUserChangeForm
from accounts.models import CustomUser


# Register your models here.
@admin.register(CustomUser)
class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = CustomUser
    list_display = ('email', 'first_name', 'last_name', 'is_staff', 'is_active')
    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        ('Info', {'fields': ('first_name', 'last_name')}),
        ('permissions', {'fields': ('is_staff', 'is_active', 'groups', 'user_permissions')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'password1', 'password2', 'is_staff', 'is_active')}
         ),
    )
    ordering = ('email',)
    search_fields = ('email', 'first_name', 'last_name')
    ordering = ('email',)