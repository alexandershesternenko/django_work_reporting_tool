# Generated by Django 4.1.1 on 2022-09-18 18:57

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('ReportingTool', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='structuraldivisions',
            name='curator',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='curator_of_SD', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='structuraldivisions',
            name='head',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='head_of_SD', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='structuraldivisions',
            name='management_unit_id',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='ReportingTool.structuraldivisions'),
        ),
        migrations.AddField(
            model_name='profession',
            name='category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ReportingTool.professioncategory'),
        ),
    ]
