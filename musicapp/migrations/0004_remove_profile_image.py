# Generated by Django 4.1.4 on 2023-01-06 08:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('musicapp', '0003_alter_songs_image'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='image',
        ),
    ]
