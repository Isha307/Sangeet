# Generated by Django 3.1.6 on 2022-04-21 09:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Sangeet', '0006_song_release'),
    ]

    operations = [
        migrations.RenameField(
            model_name='song',
            old_name='artist',
            new_name='album',
        ),
    ]