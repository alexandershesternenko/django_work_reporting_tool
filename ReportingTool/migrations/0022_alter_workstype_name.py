# Generated by Django 4.1.1 on 2022-09-25 13:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ReportingTool', '0021_completedwork_checked_by_head_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='workstype',
            name='name',
            field=models.CharField(max_length=120),
        ),
    ]
