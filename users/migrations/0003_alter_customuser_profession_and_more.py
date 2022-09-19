# Generated by Django 4.1.1 on 2022-09-19 14:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('ReportingTool', '0002_initial'),
        ('users', '0002_alter_customuser_profession_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='profession',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='ReportingTool.profession'),
        ),
        migrations.AlterField(
            model_name='customuser',
            name='struct_division',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='ReportingTool.structuraldivisions'),
        ),
    ]
