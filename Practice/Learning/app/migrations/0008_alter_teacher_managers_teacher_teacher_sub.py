# Generated by Django 5.1.1 on 2024-09-25 11:34

import django.db.models.manager
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0007_alter_teacher_options_alter_dean_managers'),
    ]

    operations = [
        migrations.AlterModelManagers(
            name='teacher',
            managers=[
                ('teacher', django.db.models.manager.Manager()),
            ],
        ),
        migrations.AddField(
            model_name='teacher',
            name='teacher_sub',
            field=models.CharField(max_length=200, null=True),
        ),
    ]