import django_filters
from ReportingTool.models.completed_work import CompletedWork


class CompletedWorkFilter(django_filters.FilterSet):

    SORT_BY_ = (
        ('worker__struct_division+', 'SD(A-Z)'),
        ('worker__struct_division-', 'SD(Z-A)'),
        ('worker+', 'Worker(A-Z)'),
        ('worker-', 'Worker(Z-A)'),
        ('work_done+', 'Work(A-Z)'),
        ('work_done-', 'Work(Z-A)'),
        ('period+', 'Date (0-9)'),
        ('period-', 'Date (9-0)'),
    )

    sort = django_filters.ChoiceFilter(label='Order by:', choices=SORT_BY_,
                                       method='filter_')
    class Meta:
        model = CompletedWork
        fields = {
            'period': ['exact', ],
            'checked_by_head': ['exact', ],
            'worker__struct_division': ['exact', ],
            'worker': ['exact', ],
            'work_done': ['exact', ],
        }

    def filter_(self, queryset, name, value):
        if value == 'worker__struct_division+':
            sort = 'worker__struct_division'
        elif value == 'worker__struct_division-':
            sort = '-worker__struct_division'
        elif value == 'worker+':
            sort = 'worker'
        elif value == 'worker-':
            sort = '-worker'
        elif value == 'work_done+':
            sort = 'work_done'
        elif value == 'work_done-':
            sort = '-work_done'
        elif value == 'period+':
            sort = 'period'
        elif value == 'period-':
            sort = '-period'
        return queryset.order_by(sort)


class CompletedWorkReportFilter(django_filters.FilterSet):

    SORT_BY_ = (
        ('worker__struct_division+', 'SD(A-Z)'),
        ('worker__struct_division-', 'SD(Z-A)'),
        ('worker+', 'Worker(A-Z)'),
        ('worker-', 'Worker(Z-A)'),
        ('work_done+', 'Work(A-Z)'),
        ('work_done-', 'Work(Z-A)'),
        ('period+', 'Date (0-9)'),
        ('period-', 'Date (9-0)'),
    )

    sort = django_filters.ChoiceFilter(label='Order by:', choices=SORT_BY_,
                                       method='filter_')
    class Meta:
        model = CompletedWork
        fields = {
            'period': ['exact', ],
            'checked_by_head': ['exact', ],
            'worker__struct_division': ['exact', ],
            'worker': ['exact', ],
            'work_done': ['exact', ],
        }


    def filter_(self, queryset, name, value):
        if value == 'worker__struct_division+':
            sort = 'worker__struct_division'
        elif value == 'worker__struct_division-':
            sort = '-worker__struct_division'
        elif value == 'worker+':
            sort = 'worker'
        elif value == 'worker-':
            sort = '-worker'
        elif value == 'work_done+':
            sort = 'work_done'
        elif value == 'work_done-':
            sort = '-work_done'
        elif value == 'period+':
            sort = 'period'
        elif value == 'period-':
            sort = '-period'
        return queryset.order_by(sort)


