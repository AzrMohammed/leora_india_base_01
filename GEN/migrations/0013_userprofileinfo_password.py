# Generated by Django 2.2.6 on 2020-11-27 21:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('GEN', '0012_auto_20201128_0237'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofileinfo',
            name='password',
            field=models.CharField(default='NONE', max_length=16),
        ),
    ]
