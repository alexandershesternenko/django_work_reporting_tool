import datetime
from django.conf import settings
from django.db import models
from django.utils.translation import gettext_lazy as _
from . import directory


class CompletedWork(models.Model):
    period = models.ForeignKey(directory.Period,
                               on_delete=models.CASCADE,
                               )
    worker = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='worker_do', default=settings.AUTH_USER_MODEL
    )
    work_done = models.ForeignKey(directory.WorksType, on_delete=models.CASCADE)
    work_scope = models.FloatField(blank=True, null=True)
    work_notes = models.CharField(_("Comments"), max_length=25, blank=True, null=True)
    record_author = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='author_of_record', auto_created=True,
    )
    record_date = models.DateTimeField(auto_now=True)

    # def save_model(self, request, obj, form, change):
    #     obj.record_author = request.user
    #     super().save(request, obj, form, change)

    def __repr__(self):
        return f'{self.period}, {self.worker}, {self.work_done}'

    def __str__(self):
        return self.__repr__()
