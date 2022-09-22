from django import forms
from ..models import CustomUser


class CustomUserCreateForm(forms.ModelForm):
    password = forms.CharField(label='Пароль', widget=forms.PasswordInput)

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
            'date_joined',
        )

