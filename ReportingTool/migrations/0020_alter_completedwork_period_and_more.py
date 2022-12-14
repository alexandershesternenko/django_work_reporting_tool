# Generated by Django 4.1.1 on 2022-09-23 18:31

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('ReportingTool', '0019_alter_completedwork_period'),
    ]

    operations = [
        migrations.AlterField(
            model_name='completedwork',
            name='period',
            field=models.ForeignKey(on_delete=models.SET('deleted date'), to='ReportingTool.period'),
        ),
        migrations.AlterField(
            model_name='completedwork',
            name='record_author',
            field=models.ForeignKey(auto_created=True, on_delete=models.SET('deleted user'), related_name='author_of_record', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='completedwork',
            name='work_done',
            field=models.ForeignKey(on_delete=models.SET('deleted works type'), to='ReportingTool.workstype'),
        ),
        migrations.AlterField(
            model_name='completedwork',
            name='worker',
            field=models.ForeignKey(default='users.CustomUser', on_delete=models.SET('deleted worker'), related_name='worker_do', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='profession',
            name='name',
            field=models.CharField(max_length=70, verbose_name='Profession'),
        ),
        migrations.AlterField(
            model_name='structuraldivisions',
            name='curator',
            field=models.ForeignKey(blank=True, null=True, on_delete=models.SET('deleted user'), related_name='curator_of_SD', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='structuraldivisions',
            name='head',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='head_of_SD', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='structuraldivisions',
            name='management_unit',
            field=models.ForeignKey(blank=True, null=True, on_delete=models.SET('deleted structural divison'), to='ReportingTool.structuraldivisions'),
        ),
        migrations.AlterField(
            model_name='workstype',
            name='measure',
            field=models.ForeignKey(blank=True, null=True, on_delete=models.SET('deleted measure'), to='ReportingTool.workstypemeasure'),
        ),
    ]
