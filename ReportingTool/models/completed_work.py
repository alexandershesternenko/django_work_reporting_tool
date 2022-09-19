from django.conf import settings
from django.db import models

from . import directory


class CompletedWork(models.Model):
    period = models.ForeignKey(directory.Period, on_delete=models.CASCADE)
    worker = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='worker_do'
    )
    work_done = models.ForeignKey(directory.WorksType, on_delete=models.CASCADE)
    record_author = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='author_of_record'
    )
    record_date = models.DateTimeField(auto_now_add=True)

    def __repr__(self):
        return self.period, self.worker, self.work_done

    def __str__(self):
        return str(self.__repr__())
