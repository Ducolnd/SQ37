# Generated by Django 2.2 on 2019-04-24 13:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_users_name'),
    ]

    operations = [
        migrations.RenameField(
            model_name='users',
            old_name='name',
            new_name='firstName',
        ),
        migrations.AddField(
            model_name='users',
            name='ied',
            field=models.CharField(default='geen', max_length=200, verbose_name='name'),
        ),
        migrations.AddField(
            model_name='users',
            name='profilePhoto',
            field=models.CharField(default='geen', max_length=200, verbose_name='name'),
        ),
        migrations.AddField(
            model_name='users',
            name='secondName',
            field=models.CharField(default='geen', max_length=200, verbose_name='name'),
        ),
    ]
