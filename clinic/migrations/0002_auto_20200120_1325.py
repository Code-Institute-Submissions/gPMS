# Generated by Django 2.2.9 on 2020-01-20 13:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clinic', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='clinic',
            name='lat',
            field=models.FloatField(default=12.0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='clinic',
            name='lng',
            field=models.FloatField(default=12.0),
            preserve_default=False,
        ),
    ]
