# Generated by Django 3.0.2 on 2020-04-29 12:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0003_auto_20200429_1213'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='consent',
        ),
    ]