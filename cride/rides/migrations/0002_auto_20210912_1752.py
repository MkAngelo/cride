# Generated by Django 2.0.9 on 2021-09-12 17:52

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('rides', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='ride',
            name='passengers',
        ),
        migrations.AddField(
            model_name='ride',
            name='passengers',
            field=models.ManyToManyField(related_name='passengers', to=settings.AUTH_USER_MODEL),
        ),
    ]
