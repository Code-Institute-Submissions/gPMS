# Generated by Django 3.0.1 on 2020-01-18 19:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('clinic', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='clinic',
            name='location',
        ),
    ]
