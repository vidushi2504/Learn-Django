# Generated by Django 3.1.1 on 2020-11-17 07:55

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('user', '0008_auto_20201117_1320'),
    ]

    operations = [
        migrations.AlterField(
            model_name='like',
            name='user',
            field=models.ManyToManyField(to=settings.AUTH_USER_MODEL),
        ),
    ]
