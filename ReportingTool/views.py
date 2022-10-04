import csv
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.db.models import Q
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views import View

from ReportingTool.forms.completed_work_forms import CompletedWorkForm
from ReportingTool.models.completed_work import CompletedWork
from ReportingTool.models.directory import StructuralDivisions, WorksType
from django.views.generic import CreateView, UpdateView, DeleteView

from users.models import CustomUser


def index(request):
    return render(request, 'index.html')


class CreateCompletedWorkView(LoginRequiredMixin, SuccessMessageMixin, CreateView):
    model = CompletedWork
    form_class = CompletedWorkForm
    template_name = 'completed_work_add.html'
    success_url = reverse_lazy('completed_work_list')
    success_message = f'Record successfully added'

    def get_form_kwargs(self):
        kwargs = super(CreateCompletedWorkView, self).get_form_kwargs()
        kwargs['user'] = self.request.user
        return kwargs

    def form_valid(self, form):
        form.instance.record_author = self.request.user
        return super().form_valid(form)


class EditCompletedWorkView(LoginRequiredMixin, SuccessMessageMixin, UpdateView):
    model = CompletedWork
    form_class = CompletedWorkForm
    template_name = 'completed_work_edit.html'
    context_object_name = 'editcompletedwork'
    success_url = None
    success_message = 'Record successfully updated'

    def get_form_kwargs(self):
        kwargs = super(EditCompletedWorkView, self).get_form_kwargs()
        kwargs['user'] = self.request.user
        return kwargs

    def get(self, request, *args, **kwargs):
        print(self)
        EditCompletedWorkView.success_url = request.META.get('HTTP_REFERER')
        return super().get(request, *args, **kwargs)


class DeleteCompletedWorkView(LoginRequiredMixin, SuccessMessageMixin, DeleteView):
    model = CompletedWork
    template_name = 'completed_work_delete.html'
    context_object_name = 'deletecompletedwork'
    success_url = reverse_lazy('completed_work_accept')
    success_message = 'Record successfully deleted'

    def get(self, request, *args, **kwargs):
        print(self)
        DeleteCompletedWorkView.success_url = request.META.get('HTTP_REFERER')
        return super().get(request, *args, **kwargs)


class AcceptCompletedWorkView(LoginRequiredMixin, View):
    model = CompletedWork

    def post(self, request, *args, **kwargs):
        completed_work_record = self.model.objects.get(id=kwargs['pk'])
        completed_work_record.checked_by_head = True
        completed_work_record.save()
        return redirect(reverse_lazy('completed_work_check'))


class RejectCompletedWorkView(LoginRequiredMixin, View):
    model = CompletedWork

    def post(self, request, *args, **kwargs):
        completed_work_record = self.model.objects.get(id=kwargs['pk'])
        completed_work_record.checked_by_head = False
        completed_work_record.save()
        return redirect(reverse_lazy('reports_related_struct_unit'))


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
    return response


def get_current_user(request):
    current_user = request.user
    return current_user


def is_valid_query_param(param):
    return param != '' and param is not None


def reports_related(request):
    return render(request, 'reports_related_struct_unit.html')

def ReportsFilterView(request):
    user = get_current_user(request)
    qs = CompletedWork.objects.filter(checked_by_head=True).filter(
        Q(worker__struct_division__head=user) |
        Q(worker__struct_division__management_unit__head=user) |
        Q(worker__struct_division__curator=user) |
        Q(worker__struct_division__management_unit__curator=user)
    )
    struct_divisions = StructuralDivisions.objects.filter(
        Q(head=user) |
        Q(management_unit__head=user) |
        Q(curator=user) |
        Q(management_unit__curator=user)
    )
    workers = CustomUser.objects.filter(
        Q(struct_division__head=user) |
        Q(struct_division__management_unit__head=user) |
        Q(struct_division__curator=user) |
        Q(struct_division__management_unit__curator=user)
    )
    workstype = WorksType.objects.filter(
        Q(available_to__head=user) |
        Q(available_to__curator=user)
    ).distinct()

    work_notes_contains_query = request.GET.get('work_notes_contains')
    work_scope_min = request.GET.get('work_scope_min')
    work_scope_max = request.GET.get('work_scope_max')
    period_min = request.GET.get('period_min')
    period_max = request.GET.get('period_max')
    struct_division = request.GET.get('struct_division')

    # special for worker
    worker = request.GET.get('worker')

    if worker and worker != 'Choose...':
        middle_name = None

        try:
            last_name, first_name, middle_name = worker.split()
            try:
                worker_get_id = CustomUser.objects.get(last_name=last_name,
                                                       first_name=first_name,
                                                       middle_name=middle_name)
            except  ValueError:
                worker_get_id = None

        except ValueError:
            last_name, first_name = worker.split()
            worker_get_id = CustomUser.objects.get(last_name=last_name,
                                                   first_name=first_name)


    work_done = request.GET.get('work_done')

    if is_valid_query_param(work_notes_contains_query):
        qs = qs.filter(work_notes__icontains=work_notes_contains_query)

    if is_valid_query_param(work_scope_min):
        qs = qs.filter(work_scope__gte=work_scope_min)

    if is_valid_query_param(work_scope_max):
        qs = qs.filter(work_scope__lte=work_scope_max)

    if is_valid_query_param(period_min):
        qs = qs.filter(period__date__gte=period_min)

    if is_valid_query_param(period_max):
        qs = qs.filter(period__date__lte=period_max)

    if is_valid_query_param(struct_division) and struct_division != 'Choose...':
        qs = qs.filter(worker__struct_division__name=struct_division)

    if worker:
        if is_valid_query_param(worker) and worker != 'Choose...':
            qs = qs.filter(worker=worker_get_id)

    if is_valid_query_param(work_done) and work_done != 'Choose...':
        qs = qs.filter(work_done__name=work_done).filter(
            Q(worker__struct_division__head=user) |
            Q(worker__struct_division__management_unit__head=user) |
            Q(worker__struct_division__curator=user) |
            Q(worker__struct_division__management_unit__curator=user)
        )

    context = {
        'queryset': qs,
        'struct_divisions': struct_divisions,
        'workers': workers,
        'workstype': workstype,
    }

    if 'button_export' in request.GET:
        return export_report(request)

    return render(request, 'reports_related_struct_unit.html', context)
