from django.contrib import admin
import ReportingTool.models.directory as direct
from ReportingTool.models.completed_work import CompletedWork


admin.site.register(direct.ProfessionCategory)
admin.site.register(direct.Profession)
admin.site.register(direct.Period)
admin.site.register(direct.StructuralDivisions)
admin.site.register(direct.WorksTypeMeasure)
admin.site.register(direct.WorksType)
admin.site.register(CompletedWork)

