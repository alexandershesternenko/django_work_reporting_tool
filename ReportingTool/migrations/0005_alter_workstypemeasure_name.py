# Generated by Django 4.1.1 on 2022-09-19 19:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ReportingTool', '0004_alter_structuraldivisions_options'),
    ]

    operations = [
        migrations.AlterField(
            model_name='workstypemeasure',
            name='name',
            field=models.CharField(max_length=20),
        ),
    ]
