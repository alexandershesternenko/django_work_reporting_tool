from django.conf import settings
from django.db import models
import directory
from ...users.models import CustomUser


class CompletedWork(models.Model):
    period = models.ForeignKey(directory.Period, on_delete=models.CASCADE)
    worker = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    work_done = models.ForeignKey(directory.WorksType, on_delete=models.CASCADE)
    record_author = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
    )
    record_date = models.DateTimeField(auto_now_add=True)

    def __repr__(self):
        return self.period, self.worker, self.work_done

    def __str__(self):
        return self.__repr__()
