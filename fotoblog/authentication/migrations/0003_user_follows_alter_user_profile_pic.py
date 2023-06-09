# Generated by Django 4.1.7 on 2023-03-19 19:02

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0002_auto_20230319_1810'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='follows',
            field=models.ManyToManyField(limit_choices_to={'role': 'CREATOR'}, to=settings.AUTH_USER_MODEL, verbose_name='suit'),
        ),
        migrations.AlterField(
            model_name='user',
            name='profile_pic',
            field=models.ImageField(blank=True, null=True, upload_to='', verbose_name='Photo de profil'),
        ),
    ]
