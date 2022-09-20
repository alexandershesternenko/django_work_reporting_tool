from django.db import models
from django.conf import settings


class ProfessionCategory(models.Model):
    name = models.CharField(max_length=50)

    class Meta:
        verbose_name_plural = "Profession categories"

    def __repr__(self):
        return self.name

    def __str__(self):
        return self.__repr__()


class Profession(models.Model):
    name = models.CharField(max_length=70)
    category = models.ForeignKey(ProfessionCategory, on_delete=models.CASCADE)

    class Meta:
        ordering = ('name', )

    def __repr__(self):
        return self.name

    def __str__(self):
        return f'{self.name}'


class Period(models.Model):
    date = models.DateField()

    def __repr__(self):
        return self.date

    def __str__(self):
        return str(self.__repr__())


class StructuralDivisions(models.Model):
    name = models.CharField(max_length=70)
    management_unit = models.ForeignKey('self', on_delete=models.CASCADE, blank=True, null=True)
    head = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE, related_name='head_of_SD', blank=True, null=True
    )
    curator = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE, related_name='curator_of_SD', blank=True, null=True
    )

    class Meta:
        verbose_name_plural = "Structural division"
        ordering = ('name',)

    def __repr__(self):
        return self.pk, self.name, self.management_unit_id

    def __str__(self):
        return str(self.name)


class WorksTypeMeasure(models.Model):
    name = models.CharField(max_length=20)

    def __repr__(self):
        return self.name

    def __str__(self):
        return self.__repr__()


class WorksType(models.Model):
    name = models.CharField(max_length=100)
    available_to = models.ManyToManyField(StructuralDivisions)
    time_norm = models.FloatField(blank=True, null=True)  # man-hours
    measure = models.ForeignKey(WorksTypeMeasure, on_delete=models.CASCADE, blank=True, null=True)

    class Meta:
        ordering = ('name',)

    def __repr__(self):
        return self.name

    def __str__(self):
        return self.__repr__()
