from django.contrib import admin
from django_admin_listfilter_dropdown.filters import RelatedDropdownFilter, DropdownFilter

from users.models import CustomUser
from users.forms.custom_user import CustomUserCreateForm


class CustomUserAdmin(admin.ModelAdmin):
    form = CustomUserCreateForm
    model = CustomUser
    list_display = ['username', 'last_name', 'first_name', 'middle_name',
                    'id', 'profession', 'struct_division',
                    'email', 'is_active', 'last_login', ]
    list_filter = (
        ('struct_division', RelatedDropdownFilter),
        ('profession', RelatedDropdownFilter),
        ('is_active', DropdownFilter),
    )
    ordering = ['username', 'last_name', 'first_name', 'middle_name']
    search_fields = ('last_name', 'first_name', 'middle_name',)
    readonly_fields = []

    def get_fields(self, request, obj=None):
        fields = super().get_fields(request, obj)
        if obj:
            fields.extend(['groups', 'user_permissions'])
        return fields

    def get_readonly_fields(self, request, obj=None):
        if obj:
            return self.readonly_fields + ['password', 'date_joined']
        return self.readonly_fields


admin.site.register(CustomUser, CustomUserAdmin)


