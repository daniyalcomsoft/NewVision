# Generated by Django 2.1.1 on 2018-09-18 16:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('students', '0006_auto_20180918_2147'),
    ]

    operations = [
        migrations.AddField(
            model_name='gr_register',
            name='status',
            field=models.CharField(choices=[('P', 'Present'), ('FM', 'Left')], default='P', max_length=10),
        ),
    ]
