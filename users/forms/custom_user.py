from django import forms
from ..models import CustomUser


class CustomUserForm(forms.ModelForm):
    class Meta:
        model = CustomUser
        fields = (
            'username',
            'password',
            'last_name',
            'first_name',
            'middle_name',
            'profession',
            'struct_division',
            'email',
            'is_active',
        )
