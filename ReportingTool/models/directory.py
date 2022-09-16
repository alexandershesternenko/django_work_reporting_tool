from django.db import models
import staff


class ProfessionCategory(models.Model):
    name = models.CharField(max_length=50)

    def __repr__(self):
        return self.name

    def __str__(self):
        return self.__repr__()


class Profession(models.Model):
    name = models.CharField(max_length=70)
    category = models.ForeignKey(ProfessionCategory, on_delete=models.CASCADE)

    def __repr__(self):
        return self.name

    def __str__(self):
        return self.__repr__()


class Period(models.Model):
    date = models.DateField()

    def __repr__(self):
        return self.date

    def __str__(self):
        return self.__repr__()


class StructuralDivisions(models.Model):
    name = models.CharField(max_length=70)
    management_unit_id = models.ForeignKey('self', on_delete=models.CASCADE, blank=True)
    head = models.ForeignKey(staff.Employees, on_delete=models.CASCADE, blank=True)
    curator = models.ForeignKey(staff.Employees, on_delete=models.CASCADE, blank=True)

    def __repr__(self):
        return self.name

    def __str__(self):
        return self.__repr__()


class WorksTypeMeasure (models.Model):
    name = models.CharField(max_length=10)

    def __repr__(self):
        return self.name

    def __str__(self):
        return self.__repr__()


class WorksType(models.Model):
    name = models.CharField(max_length=100)
    time_norm = models.FloatField(blank=True)  # man-hours
    measure = models.CharField(WorksTypeMeasure, blank=True)

    def __repr__(self):
        return self.name

    def __str__(self):
        return self.__repr__()
