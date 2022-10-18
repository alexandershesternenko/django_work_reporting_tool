import django_filters
from django import forms

from ReportingTool.models.completed_work import CompletedWork
from ReportingTool.models.directory import *
from ReportingTool.widget import DatePickerInput


class CompletedWorkFilter(django_filters.FilterSet):

    class Meta:
        model = CompletedWork
        fields = {
            'period': ['exact', ],
            'checked_by_head': ['exact', ],
            'worker__struct_division': ['exact', ],
            'worker': ['exact', ],
            'work_done': ['exact', ],
        }

class CompletedWorkReportFilter(django_filters.FilterSet):

    class Meta:
        model = CompletedWork
        fields = {
            'period': ['exact', ],
            'checked_by_head': ['exact', ],
            'worker__struct_division': ['exact', ],
            'worker': ['exact', ],
            'work_done': ['exact', ],
        }


class UserFilter(django_filters.FilterSet):
    # first_name = django_filters.CharFilter(lookup_expr='icontains')
    # year_joined = django_filters.NumberFilter(name='date_joined', lookup_expr='year')
    period = django_filters.FilterSet(queryset=Period.objects.all())

    class Meta:
        model = CompletedWork
        fields = ['period', 'checked_by_head', 'worker__struct_division', 'work_done']