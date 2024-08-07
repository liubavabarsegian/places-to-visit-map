# Generated by Django 5.0.6 on 2024-07-12 22:41

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('map', '0005_alter_point_fixed'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AddField(
            model_name='point',
            name='favorited_by',
            field=models.ManyToManyField(blank=True, related_name='favorite_points', to=settings.AUTH_USER_MODEL),
        ),
    ]
