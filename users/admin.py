from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .forms.custom_user import CustomUserCreationForm, CustomUserChangeForm
from .models import CustomUser


class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = CustomUser
    list_display = ['username', 'first_name', 'last_name', 'profession', 'struct_division', 'email', ]


admin.site.register(CustomUser, CustomUserAdmin)
