# Generated by Django 4.1.1 on 2022-09-19 20:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ReportingTool', '0008_alter_structuraldivisions_options'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='profession',
            options={'ordering': ('-category', 'name')},
        ),
    ]
