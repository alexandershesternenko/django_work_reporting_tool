from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.urls import reverse_lazy

from ReportingTool.forms.completed_work_forms import CompletedWorkForm
from ReportingTool.models.completed_work import CompletedWork
from django.views.generic import CreateView

from ReportingTool.models.directory import WorksType


def index(request):
    return render(request, 'index.html')


class CreateCompletedWorkView(LoginRequiredMixin, CreateView):
    model = CompletedWork
    form_class = CompletedWorkForm
    template_name = 'completed_work_add.html'
    permission_required = ('ReportingTool.add_completed_work', 'ReportingTool.view_completed_work',)
    success_url = reverse_lazy('completed_work_list')

    def get_form_kwargs(self):
        kwargs = super(CreateCompletedWorkView, self).get_form_kwargs()
        kwargs['user'] = self.request.user
        return kwargs

    def form_valid(self, form):
        form.instance.record_author = self.request.user
        return super().form_valid(form)


def reports(request):
    return render(request, 'reports.html')
