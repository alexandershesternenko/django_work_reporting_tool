# Generated by Django 4.1.1 on 2022-09-21 18:30

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('ReportingTool', '0016_completedwork_work_scope_alter_completedwork_period_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='completedwork',
            name='period',
            field=models.ForeignKey(default=datetime.datetime(2022, 9, 21, 18, 30, 44, 495151, tzinfo=datetime.timezone.utc), on_delete=django.db.models.deletion.CASCADE, to='ReportingTool.period'),
        ),
    ]
