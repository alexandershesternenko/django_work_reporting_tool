from django import forms
from ReportingTool.models.completed_work import *


class CompletedWorkForm(forms.ModelForm):
    class Meta:
        model = CompletedWork
        fields = '__all__'
        exclude = ('record_author', 'record_date', )



    # def __init__(self, *args, **kwargs):
    #     if kwargs.get('record_author'):
    #         self.user = kwargs.pop('record_author')
    #     super(CompletedWorkForm, self).__init__(*args, **kwargs)
    #
    # def save(self, *args, **kwargs):
    #     obj = super(CompletedWorkForm, self).save(commit=False)
    #     obj.record_author = self.user
    #     obj.save()
    #     return obj
