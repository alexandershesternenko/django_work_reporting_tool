from django.urls import path, include
from ReportingTool import views

urlpatterns = [

    path("", views.index, name='index'),
]
