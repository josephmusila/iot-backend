# Generated by Django 3.2.13 on 2022-09-07 11:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_auto_20220805_2117'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sensors',
            name='waterlevel',
            field=models.CharField(blank=True, max_length=5, null=True),
        ),
    ]
