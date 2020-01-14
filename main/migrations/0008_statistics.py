# Generated by Django 2.2.1 on 2019-05-06 06:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0007_users_athlete'),
    ]

    operations = [
        migrations.CreateModel(
            name='statistics',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('biggest_ride_distance', models.IntegerField(default=0, verbose_name='biggest_ride_distance')),
                ('biggest_climb_elevation_gain', models.IntegerField(default=0, verbose_name='biggest_climb_elevation_gain')),
                ('total_distance', models.IntegerField(default=0, verbose_name='total_distance')),
                ('total_elevation_gain', models.IntegerField(default=0, verbose_name='total_elevation_gain')),
                ('total_moving_time', models.IntegerField(default=0, verbose_name='total_moving_time')),
                ('total_count', models.IntegerField(default=0, verbose_name='total_count')),
                ('ytd_count', models.IntegerField(default=0, verbose_name='ytd_count')),
                ('ytd_distance', models.IntegerField(default=0, verbose_name='ytd_distance')),
                ('ytd_moving_time', models.IntegerField(default=0, verbose_name='ytd_moving_time')),
                ('ytd_elevation_gain', models.IntegerField(default=0, verbose_name='ytd_elevation_gain')),
            ],
        ),
    ]