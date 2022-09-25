from .custom_user import CustomUserCreateForm
from ..models import CustomUser


class SignUpForm(CustomUserCreateForm):

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
        )
