# Generated by Django 4.1.1 on 2022-09-21 09:28

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('ReportingTool', '0015_alter_profession_options_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='completedwork',
            name='work_scope',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='completedwork',
            name='period',
            field=models.ForeignKey(default=datetime.date(2022, 9, 21), on_delete=django.db.models.deletion.CASCADE, to='ReportingTool.period'),
        ),
        migrations.AlterField(
            model_name='completedwork',
            name='record_author',
            field=models.ForeignKey(auto_created=True, on_delete=django.db.models.deletion.CASCADE, related_name='author_of_record', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='completedwork',
            name='record_date',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AlterField(
            model_name='completedwork',
            name='worker',
            field=models.ForeignKey(default='users.CustomUser', on_delete=django.db.models.deletion.CASCADE, related_name='worker_do', to=settings.AUTH_USER_MODEL),
        ),
    ]
