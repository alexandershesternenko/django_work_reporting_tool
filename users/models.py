from django.contrib.auth.models import AbstractUser, PermissionsMixin
from django.contrib.auth.validators import UnicodeUsernameValidator
from django.db import models
from django.utils import timezone
from django.utils.translation import gettext_lazy as _
from ReportingTool.models import directory
from ReportingTool.models.directory import StructuralDivisions


class CustomUser(AbstractUser, PermissionsMixin):
    username_validator = UnicodeUsernameValidator()

    username = models.CharField(_("Username"), max_length=100,
                                unique=True,
                                validators=[username_validator],
                                error_messages={
                                    "unique": _("A user with that username already exists."),
                                },
                                help_text=_("example: ShevchenkoTG")
                                )
    first_name = models.CharField(_("First name"), max_length=25)
    last_name = models.CharField(_("Last name"), max_length=25)
    middle_name = models.CharField(_("Middle name"), max_length=25, blank=True)
    email = models.EmailField(_("Email"), blank=True)
    profession = models.ForeignKey(directory.Profession,
                                   on_delete=models.SET('deleted profession'),
                                   verbose_name=_("Profession"), blank=True, null=True)
    struct_division = models.ForeignKey(directory.StructuralDivisions,
                                        on_delete=models.SET('deleted structural division'),
                                        verbose_name=_("Structural Divisions"), blank=True, null=True)
    date_joined = models.DateTimeField(_("date joined"), default=timezone.now)
    is_active = models.BooleanField(_("active"), default=False)

    def is_head(self):
        if StructuralDivisions.objects.filter(head=self.pk):
            return True
        return False

    def is_curator(self):
        if StructuralDivisions.objects.filter(curator=self.pk):
            return True
        return False

    def __repr__(self):
        return f'{self.last_name} {self.first_name} {self.middle_name}'

    def __str__(self):
        return f'{self.last_name} {self.first_name} {self.middle_name}'



