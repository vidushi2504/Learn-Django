# Generated by Django 3.1.1 on 2020-11-12 05:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0004_like'),
    ]

    operations = [
        migrations.RenameField(
            model_name='profile',
            old_name='user',
            new_name='username',
        ),
    ]
