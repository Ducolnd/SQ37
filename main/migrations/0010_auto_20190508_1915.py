# Generated by Django 2.2.1 on 2019-05-08 17:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0009_statistics_athlete'),
    ]

    operations = [
        migrations.AddField(
            model_name='statistics',
            name='recent_count',
            field=models.IntegerField(default=0, verbose_name='recent_count'),
        ),
        migrations.AddField(
            model_name='statistics',
            name='recent_distance',
            field=models.IntegerField(default=0, verbose_name='recent_distance'),
        ),
        migrations.AddField(
            model_name='statistics',
            name='recent_elevation_gain',
            field=models.IntegerField(default=0, verbose_name='recent_elevation_gain'),
        ),
        migrations.AddField(
            model_name='statistics',
            name='recent_moving_time',
            field=models.IntegerField(default=0, verbose_name='recent_moving_time'),
        ),
    ]
