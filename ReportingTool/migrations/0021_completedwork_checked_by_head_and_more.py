# Generated by Django 4.1.1 on 2022-09-25 12:15

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('ReportingTool', '0020_alter_completedwork_period_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='completedwork',
            name='checked_by_head',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='completedwork',
            name='record_author',
            field=models.ForeignKey(auto_created=True, on_delete=models.SET('deleted user'), related_name='record_author', to=settings.AUTH_USER_MODEL),
        ),
    ]
