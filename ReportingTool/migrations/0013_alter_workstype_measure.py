# Generated by Django 4.1.1 on 2022-09-20 16:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('ReportingTool', '0012_alter_workstype_time_norm'),
    ]

    operations = [
        migrations.AlterField(
            model_name='workstype',
            name='measure',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='ReportingTool.workstypemeasure'),
        ),
    ]
