# Generated by Django 4.0.1 on 2022-01-24 18:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_profile_location_skill'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='social_twitter',
        ),
        migrations.RemoveField(
            model_name='profile',
            name='social_youtube',
        ),
    ]
