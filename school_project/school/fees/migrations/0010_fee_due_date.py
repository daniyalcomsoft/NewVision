# Generated by Django 2.1.2 on 2018-10-20 08:16

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('fees', '0009_remove_fee_fee_amount_dues'),
    ]

    operations = [
        migrations.AddField(
            model_name='fee',
            name='due_date',
            field=models.DateField(default=django.utils.timezone.now),
        ),
    ]
