from django.contrib import admin
from .forms.custom_user import CustomUserForm
from .models import CustomUser


class CustomUserAdmin(admin.ModelAdmin):
    form = CustomUserForm
    list_display = ['username', 'last_name', 'first_name', 'middle_name',
                    'id', 'profession', 'struct_division',
                    'email', 'is_active', 'last_login', ]
    list_filter = ('struct_division', 'profession', 'is_active')
    ordering = ['last_name', 'first_name', 'middle_name']


admin.site.register(CustomUser, CustomUserAdmin)
