from django.contrib.auth.models import AbstractUser
from django.contrib.auth.validators import UnicodeUsernameValidator
from django.db import models
from django.utils import timezone
from django.utils.translation import gettext_lazy as _

from ReportingTool.models import directory


class CustomUser(AbstractUser):
    username_validator = UnicodeUsernameValidator()

    username = models.CharField(_("Ім'я користувача"), max_length=100,
                                unique=True,
                                validators=[username_validator],
                                error_messages={
                                    "unique": _("Такий обліковий запис вже є"),
                                },
                                help_text='Латинськими літерами (напр. ShevchenkoTG)'
                                )
    first_name = models.CharField(_("Ім'я"), max_length=25)
    last_name = models.CharField(_("Прізвище"), max_length=25)
    middle_name = models.CharField(_("По батькові"), max_length=25, blank=True)
    email = models.EmailField(_("Електронна пошта"), blank=True)
    profession = models.ForeignKey(directory.Profession, on_delete=models.CASCADE, verbose_name="Професія", blank=True, null=True)
    struct_division = models.ForeignKey(directory.StructuralDivisions, on_delete=models.CASCADE,
                                        verbose_name="Структурний підрозділ", blank=True, null=True)
    date_joined = models.DateTimeField(_("date joined"), default=timezone.now)
    is_active = models.BooleanField(_("Активний"), default=False)

    def __repr__(self):
        return self.last_name, self.first_name, self.middle_name

    def __str__(self):
        return f'{self.last_name} {self.first_name} {self.middle_name}'
