# Generated by Django 5.0.6 on 2024-07-12 21:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('map', '0004_alter_point_images'),
    ]

    operations = [
        migrations.AlterField(
            model_name='point',
            name='fixed',
            field=models.BooleanField(default=False, verbose_name='Подтверждено'),
        ),
    ]
