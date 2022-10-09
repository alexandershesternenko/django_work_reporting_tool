import django_filters
from ReportingTool.models.completed_work import CompletedWork


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


