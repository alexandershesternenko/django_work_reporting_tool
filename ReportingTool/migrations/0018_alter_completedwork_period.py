# Generated by Django 4.1.1 on 2022-09-21 18:44

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('ReportingTool', '0017_alter_completedwork_period'),
    ]

    operations = [
        migrations.AlterField(
            model_name='completedwork',
            name='period',
            field=models.ForeignKey(default=datetime.date(2022, 9, 21), on_delete=django.db.models.deletion.CASCADE, to='ReportingTool.period'),
        ),
    ]