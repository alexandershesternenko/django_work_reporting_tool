# Generated by Django 4.1.1 on 2022-09-20 16:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ReportingTool', '0011_workstype_available_to'),
    ]

    operations = [
        migrations.AlterField(
            model_name='workstype',
            name='time_norm',
            field=models.FloatField(blank=True, null=True),
        ),
    ]
