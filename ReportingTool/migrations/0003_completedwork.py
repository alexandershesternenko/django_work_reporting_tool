# Generated by Django 4.1.1 on 2022-09-19 18:13

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('ReportingTool', '0002_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='CompletedWork',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('record_date', models.DateTimeField(auto_now_add=True)),
                ('period', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ReportingTool.period')),
                ('record_author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='author_of_record', to=settings.AUTH_USER_MODEL)),
                ('work_done', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ReportingTool.workstype')),
                ('worker', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='worker_do', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
