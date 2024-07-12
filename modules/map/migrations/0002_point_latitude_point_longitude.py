# Generated by Django 5.0.6 on 2024-07-12 16:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('map', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='point',
            name='latitude',
            field=models.FloatField(default=0, verbose_name='Широта'),
        ),
        migrations.AddField(
            model_name='point',
            name='longitude',
            field=models.FloatField(default=0, verbose_name='Долгота'),
        ),
    ]
