# Generated by Django 4.1.1 on 2022-09-20 13:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('ReportingTool', '0010_completedwork_work_notes'),
        ('users', '0003_alter_customuser_profession_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='struct_division',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='ReportingTool.structuraldivisions', verbose_name='Structural divisions'),
        ),
    ]
