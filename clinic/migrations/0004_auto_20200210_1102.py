# Generated by Django 2.2.9 on 2020-02-10 11:02

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('clinic', '0003_auto_20200120_1329'),
    ]

    operations = [
        migrations.AlterField(
            model_name='clinic',
            name='practitioner',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
