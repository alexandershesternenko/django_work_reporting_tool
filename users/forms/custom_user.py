from django import forms
from ..models import CustomUser


class CustomUserCreateForm(forms.ModelForm):
    password = forms.CharField(label='Password', widget=forms.PasswordInput)

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

    def save(self, commit=True):
        user = super().save(commit=False)
        if self.cleaned_data.get("password"):
            user.set_password(self.cleaned_data["password"])
        if commit:
            user.save()
        return user
