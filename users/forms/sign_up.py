from .custom_user import CustomUserCreateForm
from ..models import CustomUser
from captcha.fields import ReCaptchaField
from captcha.widgets import ReCaptchaV2Checkbox


class SignUpForm(CustomUserCreateForm):
    captcha = ReCaptchaField(widget=ReCaptchaV2Checkbox())


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
            'captcha'
        )

