from django.contrib import admin

from users.models import CustomUser
from users.forms.custom_user import CustomUserCreateForm


class CustomUserAdmin(admin.ModelAdmin):
    form = CustomUserCreateForm
    model = CustomUser
    list_display = ['username', 'last_name', 'first_name', 'middle_name',
                    'id', 'profession', 'struct_division',
                    'email', 'is_active', 'last_login', ]
    list_filter = ('struct_division', 'profession', 'is_active')
    ordering = ['last_name', 'first_name', 'middle_name']
    search_fields = ('last_name', 'first_name', 'middle_name',)
    readonly_fields = []

    def get_readonly_fields(self, request, obj=None):
        if obj:
            return self.readonly_fields + ['password', 'date_joined']
        return self.readonly_fields


admin.site.register(CustomUser, CustomUserAdmin)


