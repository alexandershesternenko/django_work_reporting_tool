from django.contrib.auth.models import AbstractUser
from django.contrib.auth.validators import UnicodeUsernameValidator
from django.db import models
from django.utils import timezone
from django.utils.translation import gettext_lazy as _

from ReportingTool.models import directory


class CustomUser(AbstractUser):
    username_validator = UnicodeUsernameValidator()

    username = models.CharField(max_length=100,
                                unique=True,
                                validators=[username_validator],
                                error_messages={
                                    "unique": _("A user with that username already exists."),
                                },
                                )
    first_name = models.CharField(_("first name"), max_length=25)
    last_name = models.CharField(_("last name"), max_length=25)
    middle_name = models.CharField(_("middle name"), max_length=25, blank=True)
    email = models.EmailField(_("email address"), blank=True)
    profession = models.ForeignKey(directory.Profession, on_delete=models.CASCADE)
    struct_division = models.ForeignKey(directory.StructuralDivisions, on_delete=models.CASCADE)
    date_joined = models.DateTimeField(_("date joined"), default=timezone.now)

    def __repr__(self):
        return self.last_name, self.first_name, self.middle_name, self.struct_division, self.profession

    def __str__(self):
        return self.__repr__()
