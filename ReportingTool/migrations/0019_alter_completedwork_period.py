# Generated by Django 4.1.1 on 2022-09-22 18:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('ReportingTool', '0018_alter_completedwork_period'),
    ]

    operations = [
        migrations.AlterField(
            model_name='completedwork',
            name='period',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ReportingTool.period'),
        ),
    ]