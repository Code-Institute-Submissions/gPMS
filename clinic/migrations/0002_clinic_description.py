# Generated by Django 3.0.1 on 2020-01-13 16:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clinic', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='clinic',
            name='description',
            field=models.TextField(default='Awesome', max_length=5000),
            preserve_default=False,
        ),
    ]
