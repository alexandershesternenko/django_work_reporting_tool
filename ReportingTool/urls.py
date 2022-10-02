from django.urls import path
from django_filters.views import FilterView
from ReportingTool.filters import CompletedWorkFilter, CompletedWorkReportFilter
from ReportingTool import views
from ReportingTool.views import EditCompletedWorkView, DeleteCompletedWorkView, AcceptCompletedWorkView, \
    RejectCompletedWorkView, export_report, bootstrapFilterView

urlpatterns = [

    path('',
         FilterView.as_view(
             filterset_class=CompletedWorkFilter,
             template_name='index.html'),
         name='index'),

    path('completed_work_list',
         FilterView.as_view(
             filterset_class=CompletedWorkFilter,
             template_name='completed_work_list.html'),
         name='completed_work_list'),

    path('add',
         views.CreateCompletedWorkView.as_view(),
         name='completed_work_add'),

    path('<int:pk>/edit',
         EditCompletedWorkView.as_view(),
         name='completed_work_edit'),

    path('<int:pk>/delete', DeleteCompletedWorkView.as_view(),
         name='completed_work_delete'),

    path('completed_work_check',
         FilterView.as_view(
             filterset_class=CompletedWorkFilter,
             template_name='completed_work_check.html'),
         name='completed_work_check'),


    path('reports_related_struct_unit',
         FilterView.as_view(
             filterset_class=CompletedWorkReportFilter,
             template_name='reports_related_struct_unit.html'),
         name='reports_related_struct_unit'),

    path('<int:pk>/accept',
         AcceptCompletedWorkView.as_view(),
         name='completed_work_accept'),

    path('<int:pk>/reject',
         RejectCompletedWorkView.as_view(),
         name='completed_work_reject'),

    path('export_report',
         export_report,
         name='export_report'),

    path('boot/',
        bootstrapFilterView,
        name='boot'),

]
