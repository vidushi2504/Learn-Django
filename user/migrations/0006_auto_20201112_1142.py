# Generated by Django 3.1.1 on 2020-11-12 06:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0005_auto_20201112_1128'),
    ]

    operations = [
        migrations.RenameField(
            model_name='profile',
            old_name='username',
            new_name='user',
        ),
    ]
