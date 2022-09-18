# from django.contrib.auth.models import User
# from django.db import models
# import directory
#
#
# class Employees(models.Model):
#     user = models.OneToOneField(User, on_delete=models.CASCADE)
#     firstname = models.CharField(max_length=25)
#     lastname = models.CharField(max_length=25)
#     middle_name = models.CharField(max_length=25, blank=True)
#     profession = models.ForeignKey(directory.Profession, on_delete=models.CASCADE)
#     struct_division = models.ForeignKey(directory.StructuralDivisions, on_delete=models.CASCADE)
#
#     def __repr__(self):
#         return self.lastname, self.firstname, self.middle_name, self.profession, self.struct_division
#
#     def __str__(self):
#         return self.__repr__()

