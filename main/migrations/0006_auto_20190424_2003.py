# Generated by Django 2.2 on 2019-04-24 18:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0005_auto_20190424_1600'),
    ]

    operations = [
        migrations.AlterField(
            model_name='users',
            name='firstName',
            field=models.CharField(default='geen', max_length=200, verbose_name='firstName'),
        ),
        migrations.AlterField(
            model_name='users',
            name='ied',
            field=models.CharField(default='geen', max_length=200, verbose_name='ied'),
        ),
        migrations.AlterField(
            model_name='users',
            name='profilePhoto',
            field=models.CharField(default='geen', max_length=200, verbose_name='profilePhoto'),
        ),
        migrations.AlterField(
            model_name='users',
            name='secondName',
            field=models.CharField(default='geen', max_length=200, verbose_name='secondName'),
        ),
    ]
