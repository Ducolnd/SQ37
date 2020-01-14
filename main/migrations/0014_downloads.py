# Generated by Django 2.2.1 on 2019-05-19 15:05

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0013_auto_20190512_1710'),
    ]

    operations = [
        migrations.CreateModel(
            name='downloads',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(default='Geen titel benoemd', max_length=100, verbose_name='title')),
                ('text', models.TextField(default='Geen beschrijving benoemd', verbose_name='text')),
                ('date', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date')),
                ('file', models.FileField(upload_to='', verbose_name='file')),
            ],
        ),
    ]
