# Generated by Django 4.1.1 on 2022-09-19 20:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ReportingTool', '0007_alter_structuraldivisions_management_unit_id'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='structuraldivisions',
            options={'ordering': ('id',), 'verbose_name_plural': 'Structural Division'},
        ),
    ]
