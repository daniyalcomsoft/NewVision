# Generated by Django 2.1.2 on 2018-10-17 07:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('fees', '0003_fee_gr_num'),
    ]

    operations = [
        migrations.AddField(
            model_name='fee',
            name='fee_code',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='fees.fees_type'),
        ),
    ]
