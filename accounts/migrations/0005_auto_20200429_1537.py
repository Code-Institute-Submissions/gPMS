# Generated by Django 3.0.2 on 2020-04-29 15:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clinic', '0001_initial'),
        ('accounts', '0004_remove_profile_consent'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='clinics',
            field=models.ManyToManyField(blank=True, to='clinic.Clinic'),
        ),
    ]
