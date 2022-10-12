from django.core.mail import send_mail
from django.urls import path
from django_filters.views import FilterView
from ReportingTool.filters import CompletedWorkFilter
from ReportingTool import views
from ReportingTool.views import EditCompletedWorkView, DeleteCompletedWorkView, AcceptCompletedWorkView, \
    RejectCompletedWorkView, export_report, ToTrashCompletedWorkView, \
    reports_filter_view, completed_work_check_filter_view, trash_filter_view, RestoreCompletedWorkView, send_your_email

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

    path('completed_work_check/',
         completed_work_check_filter_view,
         name='completed_work_check'),

    path('completed_work_trash/',
         trash_filter_view,
         name='completed_work_trash'),

    path('<int:pk>/restore',
         RestoreCompletedWorkView.as_view(),
         name='completed_work_restore'),

    path('reports_related_struct_unit/',
         reports_filter_view,
         name='reports_related_struct_unit'),


    path('<int:pk>/accept',
         AcceptCompletedWorkView.as_view(),
         name='completed_work_accept'),

    path('<int:pk>/reject',
         RejectCompletedWorkView.as_view(),
         name='completed_work_reject'),

    path('<int:pk>/totrash',
         ToTrashCompletedWorkView.as_view(),
         name='completed_work_totrash'),

    path('export_report',
         export_report,
         name='export_report'),

    path('send_your_email/',
         send_your_email,
         name='send_your_email'),


]
