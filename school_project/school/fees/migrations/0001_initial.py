# Generated by Django 2.1.2 on 2018-10-17 07:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('students', '0010_auto_20181011_1602'),
    ]

    operations = [
        migrations.CreateModel(
            name='class_fees',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fees_amount', models.BigIntegerField(default=1000)),
                ('class_code', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='students.Classes')),
            ],
        ),
        migrations.CreateModel(
            name='concession_type',
            fields=[
                ('concession_code', models.AutoField(primary_key=True, serialize=False)),
                ('concession_type', models.CharField(default=1, max_length=255)),
                ('concession_percent', models.CharField(default=1, max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='fees_source',
            fields=[
                ('source_code', models.AutoField(primary_key=True, serialize=False)),
                ('source_name', models.CharField(default='source_name', max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='fees_type',
            fields=[
                ('fee_code', models.AutoField(primary_key=True, serialize=False)),
                ('fee_type', models.CharField(default=1, max_length=255)),
            ],
        ),
        migrations.AddField(
            model_name='class_fees',
            name='fee_code',
            field=models.ForeignKey(default='fee_code', on_delete=django.db.models.deletion.CASCADE, to='fees.fees_type'),
        ),
    ]
