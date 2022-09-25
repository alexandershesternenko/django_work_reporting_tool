
from django.contrib import admin

import ReportingTool.models.directory as direct
import users.models
from ReportingTool.forms.completed_work_forms import CompletedWorkForm
from ReportingTool.models.completed_work import CompletedWork
from django_admin_listfilter_dropdown.filters import (
    DropdownFilter, ChoiceDropdownFilter, RelatedDropdownFilter, RelatedOnlyDropdownFilter
)


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
    list_display = ('name', 'management_unit', 'head', 'curator')
    list_filter = (('management_unit', admin.RelatedOnlyFieldListFilter),)


class WorksTypeAdmin(admin.ModelAdmin):
    list_display = ('name', 'time_norm', 'measure',)
    list_filter = (
        ('available_to', RelatedDropdownFilter),
    )
    search_fields = ('name', 'time_norm', 'measure__name',)


class CompletedWorkAdmin(admin.ModelAdmin):
    form = CompletedWorkForm
    list_display = ['period', 'worker', 'work_done', 'work_scope', 'work_notes', 'checked_by_head',
                    'record_author', 'record_date', ]
    readonly_fields = ['record_author', 'record_date']
    list_filter = (
        ('period', RelatedOnlyDropdownFilter),
        ('worker', RelatedOnlyDropdownFilter),
        ('record_author', RelatedOnlyDropdownFilter),
        ('checked_by_head', DropdownFilter),
    )
    ordering = ['period', 'worker']
    search_fields = ('worker__last_name', 'worker__first_name', 'worker__middle_name', 'work_done__name')

    def save_model(self, request, obj, form, change):
        obj.record_author = request.user
        super().save_model(request, obj, form, change)


admin.site.register(direct.ProfessionCategory, ProfessionCategoryAdmin)
admin.site.register(direct.Profession, ProfessionAdmin)
admin.site.register(direct.Period)
admin.site.register(direct.StructuralDivisions, StructuralDivisionsAdmin)
admin.site.register(direct.WorksTypeMeasure)
admin.site.register(direct.WorksType, WorksTypeAdmin)
admin.site.register(CompletedWork, CompletedWorkAdmin)

