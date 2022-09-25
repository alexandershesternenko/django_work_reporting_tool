import django_filters
from ReportingTool.models.completed_work import CompletedWork


class CompletedWorkFilter(django_filters.FilterSet):

    SORT_BY_ = (
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
            'work_done': ['exact', ],
            'period': ['exact', ],
            'checked_by_head': ['exact', ],
        }

    def filter_(self, queryset, name, value):
        if value == 'work_done+':
            sort = 'work_done'
        elif value == 'work_done-':
            sort = '-work_done'
        elif value == 'period+':
            sort = 'period'
        elif value == 'period-':
            sort = '-period'
        return queryset.order_by(sort)

