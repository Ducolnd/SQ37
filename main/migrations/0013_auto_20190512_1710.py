# Generated by Django 2.2.1 on 2019-05-12 15:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0012_auto_20190512_1709'),
    ]

    operations = [
        migrations.AlterField(
            model_name='statistics',
            name='ied',
            field=models.IntegerField(default=0, verbose_name='ied'),
        ),
    ]
