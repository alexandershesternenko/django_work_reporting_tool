import csv
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views import View

from ReportingTool.forms.completed_work_forms import CompletedWorkForm
from ReportingTool.models.completed_work import CompletedWork
from django.views.generic import CreateView, UpdateView, DeleteView


def index(request):
    return render(request, 'index.html')


class CreateCompletedWorkView(LoginRequiredMixin, CreateView):
    model = CompletedWork
    form_class = CompletedWorkForm
    template_name = 'completed_work_add.html'
    success_url = reverse_lazy('completed_work_list')

    def get_form_kwargs(self):
        kwargs = super(CreateCompletedWorkView, self).get_form_kwargs()
        kwargs['user'] = self.request.user
        return kwargs

    def form_valid(self, form):
        form.instance.record_author = self.request.user
        return super().form_valid(form)


class EditCompletedWorkView(LoginRequiredMixin, UpdateView):
    model = CompletedWork
    form_class = CompletedWorkForm
    template_name = 'completed_work_edit.html'
    context_object_name = 'editcompletedwork'
    # permission_required = ('ReportingTool.view_completed_work', 'ReportingTool.change_completed_work',)
    success_url = None

    def get_form_kwargs(self):
        kwargs = super(EditCompletedWorkView, self).get_form_kwargs()
        kwargs['user'] = self.request.user
        return kwargs

    def get(self, request, *args, **kwargs):
        print(self)
        EditCompletedWorkView.success_url = request.META.get('HTTP_REFERER')
        return super().get(request, *args, **kwargs)


class DeleteCompletedWorkView(LoginRequiredMixin, DeleteView):
    model = CompletedWork
    # form_class = CompletedWorkForm
    template_name = 'completed_work_delete.html'
    context_object_name = 'deletecompletedwork'
    # permission_required = ('ReportingTool.view_completed_work', 'ReportingTool.change_completed_work',)
    success_url = reverse_lazy('completed_work_accept')

    def get_form_kwargs(self):
        kwargs = super(DeleteCompletedWorkView, self).get_form_kwargs()
        kwargs['user'] = self.request.user
        return kwargs

    def get(self, request, *args, **kwargs):
        print(self)
        DeleteCompletedWorkView.success_url = request.META.get('HTTP_REFERER')
        return super().get(request, *args, **kwargs)


class AcceptCompletedWorkView(LoginRequiredMixin, View):
    model = CompletedWork
    # permission_required = ('ReportingTool.view_completed_work', 'ReportingTool.change_completed_work',)

    def post(self, request, *args, **kwargs):
        completed_work_record = self.model.objects.get(id=kwargs['pk'])
        completed_work_record.checked_by_head = True
        completed_work_record.save()
        return redirect(reverse_lazy('completed_work_check'))


class RejectCompletedWorkView(LoginRequiredMixin, View):
    model = CompletedWork
    # permission_required = ('ReportingTool.view_completed_work', 'ReportingTool.change_completed_work',)

    def post(self, request, *args, **kwargs):
        completed_work_record = self.model.objects.get(id=kwargs['pk'])
        completed_work_record.checked_by_head = False
        completed_work_record.save()
        return redirect(reverse_lazy('reports_related_struct_unit'))


def reports(request):
    return render(request, 'reports_struct_unit.html')


def reports_related(request):
    return render(request, 'reports_related_struct_unit.html')


def export_report(request):
    response = HttpResponse(content_type='text/csv')
    writer = csv.writer(response)
    writer.writerow([
        'id',
        'Date',
        'Main SD',
        'SD',
        'Worker',
        'Type of work done',
        'Scope',
        'Notes',
        'Checked'
    ])

    for record in CompletedWork.objects.all().values_list(
            'work_done_id',
            'period__date',
            'worker__struct_division__management_unit__name',
            'worker__struct_division__name',
            'worker__last_name',
            'work_done__name',
            'work_scope',
            'work_notes',
            'checked_by_head'
    ):
        writer.writerow(record)

    response['Content-Disposition'] = 'attachment; filename="completed_work_list.csv"'
    # response.write(u'\ufeff'.encode('utf8'))
    return response
