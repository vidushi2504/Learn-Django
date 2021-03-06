# Generated by Django 3.1.1 on 2020-11-11 17:44

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('user', '0003_auto_20201111_1611'),
    ]

    operations = [
        migrations.CreateModel(
            name='Like',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('likes', models.IntegerField(default=0)),
                ('post', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='user.post')),
                ('user', models.ManyToManyField(related_name='Userthatliked', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
