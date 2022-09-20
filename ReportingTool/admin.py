from django.contrib import admin

import ReportingTool.models.directory as direct
import users.models
from ReportingTool.models.completed_work import CompletedWork


class ProfessionCategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'get_total_professions')

    @admin.display()
    def get_total_professions(self, obj):
        workers_count = direct.Profession.objects.filter(category=obj).count()
        return workers_count

    get_total_professions.short_description = 'Total professions'


class ProfessionAdmin(admin.ModelAdmin):
    list_display = ('name', 'get_total_employees')
    list_filter = (('category', admin.RelatedOnlyFieldListFilter),)

    @admin.display()
    def get_total_employees(self, obj):
        workers_count = users.models.CustomUser.objects.filter(profession=obj).count()
        return workers_count

    get_total_employees.short_description = 'Total employees'


class StructuralDivisionsAdmin(admin.ModelAdmin):
    list_display = ('name', 'management_unit',)
    list_filter = (('management_unit', admin.RelatedOnlyFieldListFilter),)


class WorksTypeAdmin(admin.ModelAdmin):
    list_filter = ('available_to',)


admin.site.register(direct.ProfessionCategory, ProfessionCategoryAdmin)
admin.site.register(direct.Profession, ProfessionAdmin)
admin.site.register(direct.Period)
admin.site.register(direct.StructuralDivisions, StructuralDivisionsAdmin)
admin.site.register(direct.WorksTypeMeasure)
admin.site.register(direct.WorksType, WorksTypeAdmin)
admin.site.register(CompletedWork)

