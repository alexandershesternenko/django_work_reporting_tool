from django.contrib.auth.forms import AuthenticationForm
from ..models import CustomUser
from captcha.fields import ReCaptchaField
from captcha.widgets import ReCaptchaV2Checkbox


class LoginForm(AuthenticationForm):
    captcha = ReCaptchaField(widget=ReCaptchaV2Checkbox())


    class Meta:
        model = CustomUser
        fields = (
            'username',
            'password',
            'captcha'
        )