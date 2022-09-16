from django.db import models
import directory
import staff

class CompletedWork(models.Model):
    period = models.ForeignKey(directory.Period, on_delete=models.CASCADE)
    worker = models.ForeignKey(staff.Employees, on_delete=models.CASCADE)
    work_done = models.ForeignKey(directory.WorksType, on_delete=models.CASCADE)



    def __repr__(self):
        return self.lastname, self.name, self.middle_name

    def __str__(self):
        return self.__repr__()