import datetime

from django.conf import settings
from django.db import models
from django.utils.translation import gettext_lazy as _
from . import directory


class CompletedWork(models.Model):
    period = models.ForeignKey(directory.Period,
                               on_delete=models.SET('deleted date'),
                               )
    worker = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.SET('deleted worker'),
        related_name='worker_do', default=settings.AUTH_USER_MODEL
    )
    work_done = models.ForeignKey(directory.WorksType, on_delete=models.SET('deleted works type'))
    work_scope = models.FloatField(blank=True, null=True)
    work_notes = models.CharField(_("Comments"), max_length=70, blank=True, null=True, )
    record_author = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.SET('deleted user'),
        related_name='record_author', auto_created=True,
    )
    record_date = models.DateTimeField(auto_now=True)
    checked_by_head = models.BooleanField(default=False)
    active = models.BooleanField(default=True)

    def __repr__(self):
        return f'{self.period}, {self.worker}, {self.work_done}'

    def __str__(self):
        return self.__repr__()

    def is_active(self):
        if self.active:
            return True
        return False
