# Generated by Django 3.0.1 on 2020-01-11 05:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('f1app', '0003_auto_20200109_1022'),
    ]

    operations = [
        migrations.AlterField(
            model_name='agent',
            name='country_code',
            field=models.CharField(max_length=6),
        ),
        migrations.AlterField(
            model_name='agent',
            name='emp_id',
            field=models.CharField(max_length=10),
        ),
        migrations.AlterField(
            model_name='dependemp',
            name='dep_id',
            field=models.CharField(max_length=10),
        ),
        migrations.AlterField(
            model_name='dependemp',
            name='emp_id',
            field=models.CharField(max_length=10),
        ),
    ]
