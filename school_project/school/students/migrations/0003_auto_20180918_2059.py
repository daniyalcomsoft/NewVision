# Generated by Django 2.1.1 on 2018-09-18 15:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('students', '0002_auto_20180918_2057'),
    ]

    operations = [
        migrations.AlterField(
            model_name='gardian',
            name='family_id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='gr_register',
            name='gr_no',
            field=models.IntegerField(primary_key=True, serialize=False),
        ),
    ]