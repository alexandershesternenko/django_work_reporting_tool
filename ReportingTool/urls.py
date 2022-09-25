from django.urls import path
from django_filters.views import FilterView
from ReportingTool.filters import CompletedWorkFilter
from ReportingTool import views


urlpatterns = [

    path('', FilterView.as_view(filterset_class=CompletedWorkFilter,
                                 template_name='index.html'), name='index'),
    path('completed_work_list', FilterView.as_view(filterset_class=CompletedWorkFilter,
                                template_name='completed_work_list.html'), name='completed_work_list'),
    path('add', views.CreateCompletedWorkView.as_view(), name='completed_work_add'),
    path("reports", views.reports, name='reports'),
]
