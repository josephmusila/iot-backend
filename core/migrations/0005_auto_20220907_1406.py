# Generated by Django 3.2.13 on 2022-09-07 11:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0004_alter_sensors_waterlevel'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sensors',
            name='photocell',
            field=models.CharField(blank=True, max_length=5, null=True),
        ),
        migrations.AlterField(
            model_name='sensors',
            name='soilmoisture',
            field=models.CharField(blank=True, max_length=5, null=True),
        ),
        migrations.AlterField(
            model_name='sensors',
            name='temperature',
            field=models.CharField(blank=True, max_length=5, null=True),
        ),
    ]