# Generated by Django 5.1.1 on 2024-09-25 11:19

import django.db.models.manager
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0006_alter_teacher_options'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='teacher',
            options={'ordering': ['teacher_name'], 'verbose_name': "Teacher's list"},
        ),
        migrations.AlterModelManagers(
            name='dean',
            managers=[
                ('dean', django.db.models.manager.Manager()),
            ],
        ),
    ]
