from django.db import models
from django.conf import settings


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
    head = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE, related_name='head_of_SD'
    )
    curator = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE, related_name='curator_of_SD'
    )

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
    measure = models.ForeignKey(WorksTypeMeasure, on_delete=models.CASCADE, blank=True)

    def __repr__(self):
        return self.name

    def __str__(self):
        return self.__repr__()
