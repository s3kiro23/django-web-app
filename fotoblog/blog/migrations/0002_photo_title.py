# Generated by Django 4.1.7 on 2023-03-17 11:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='photo',
            name='title',
            field=models.CharField(blank=True, max_length=128),
        ),
    ]
