# Generated by Django 2.2.6 on 2021-01-08 16:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('GEN', '0028_auto_20210105_2204'),
    ]

    operations = [
        migrations.AlterField(
            model_name='servisabledayscriteria',
            name='service_end_time',
            field=models.TimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='servisabledayscriteria',
            name='service_start_time',
            field=models.TimeField(blank=True, null=True),
        ),
    ]
