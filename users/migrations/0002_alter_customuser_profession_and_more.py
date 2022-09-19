# Generated by Django 4.1.1 on 2022-09-19 14:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('ReportingTool', '0002_initial'),
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='profession',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='ReportingTool.profession'),
        ),
        migrations.AlterField(
            model_name='customuser',
            name='struct_division',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='ReportingTool.structuraldivisions'),
        ),
    ]
