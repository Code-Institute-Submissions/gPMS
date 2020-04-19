# Generated by Django 3.0.2 on 2020-04-19 16:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('payments', '0004_auto_20200414_2007'),
    ]

    operations = [
        migrations.RenameField(
            model_name='plans',
            old_name='stripe_id',
            new_name='stripe_plan_id',
        ),
        migrations.RenameField(
            model_name='products',
            old_name='stripe_id',
            new_name='stripe_product_id',
        ),
        migrations.RenameField(
            model_name='subscription',
            old_name='stripe_customer_id',
            new_name='customer',
        ),
        migrations.AlterField(
            model_name='subscription',
            name='plan_type',
            field=models.CharField(choices=[('MONTHLY', 'Basic monthly plan (10kr/month)'), ('YEARLY', 'Two months free (100kr/year)'), ('FREE', 'Four months free (280kr/3 years)')], default='MONTHLY', max_length=15),
        ),
    ]
