# Generated by Django 2.1.1 on 2018-09-18 16:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('students', '0007_gr_register_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='gr_register',
            name='address',
            field=models.CharField(max_length=100, null=True, verbose_name='Home Address'),
        ),
    ]