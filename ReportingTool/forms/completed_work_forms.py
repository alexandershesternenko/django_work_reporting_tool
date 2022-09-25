from django import forms
from django.utils.timezone import now

from ReportingTool.models.completed_work import *
from ReportingTool.models.directory import WorksType, Period
from users.models import CustomUser


class CompletedWorkForm(forms.ModelForm):
    class Meta:
        model = CompletedWork
        fields = (
            'period',
            'worker',
            'work_done',
            'work_scope',
            'work_notes',
        )

    def __init__(self, user, *args, **kwargs):

        if kwargs.get('record_author'):
            self.user = kwargs.pop('record_author')
        super(CompletedWorkForm, self).__init__(*args, **kwargs)

        if user.struct_division:

            if user != user.struct_division.head or user != user.struct_division.curator:
                self.fields['worker'] = forms.ModelChoiceField(
                    queryset=CustomUser.objects.filter(id=user.pk)
                )
            else:
                self.fields['worker'] = forms.ModelChoiceField(
                    queryset=CustomUser.objects.filter(struct_division=user.struct_division)
                )

        else:  # if user == user.struct_division.curator:
            self.fields['worker'] = forms.ModelChoiceField(
                queryset=
                CustomUser.objects.filter(struct_division__curator=user) |
                CustomUser.objects.filter(id=user.pk)
            )

        self.fields['work_done'] = forms.ModelChoiceField(
            queryset=WorksType.objects.filter(available_to=user.struct_division)
        )

    def save(self, commit=True):
        obj = super(CompletedWorkForm, self).save(commit=False)
        if commit:
            obj.user = self.instance.record_author
            obj.save()
        return obj
