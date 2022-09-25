# Generated by Django 4.1.1 on 2022-09-23 18:31

import django.contrib.auth.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ReportingTool', '0020_alter_completedwork_period_and_more'),
        ('users', '0005_alter_customuser_is_active'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='email',
            field=models.EmailField(blank=True, max_length=254, verbose_name='Email'),
        ),
        migrations.AlterField(
            model_name='customuser',
            name='first_name',
            field=models.CharField(max_length=25, verbose_name='First name'),
        ),
        migrations.AlterField(
            model_name='customuser',
            name='last_name',
            field=models.CharField(max_length=25, verbose_name='Last name'),
        ),
        migrations.AlterField(
            model_name='customuser',
            name='middle_name',
            field=models.CharField(blank=True, max_length=25, verbose_name='Middle name'),
        ),
        migrations.AlterField(
            model_name='customuser',
            name='profession',
            field=models.ForeignKey(blank=True, null=True, on_delete=models.SET('deleted profession'), to='ReportingTool.profession', verbose_name='Profession'),
        ),
        migrations.AlterField(
            model_name='customuser',
            name='struct_division',
            field=models.ForeignKey(blank=True, null=True, on_delete=models.SET('deleted structural division'), to='ReportingTool.structuraldivisions', verbose_name='Structural Divisions'),
        ),
        migrations.AlterField(
            model_name='customuser',
            name='username',
            field=models.CharField(error_messages={'unique': 'A user with that username already exists.'}, help_text='example: ShevchenkoTG', max_length=100, unique=True, validators=[django.contrib.auth.validators.UnicodeUsernameValidator()], verbose_name='Username'),
        ),
    ]
