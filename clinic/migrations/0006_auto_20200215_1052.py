# Generated by Django 2.2.9 on 2020-02-15 10:52

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('clinic', '0005_auto_20200210_1104'),
    ]

    operations = [
        migrations.AlterField(
            model_name='clinic',
            name='practitioner',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
