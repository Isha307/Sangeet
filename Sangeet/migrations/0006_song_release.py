# Generated by Django 3.1.6 on 2022-04-20 13:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Sangeet', '0005_channel_history'),
    ]

    operations = [
        migrations.AddField(
            model_name='song',
            name='release',
            field=models.CharField(default='', max_length=2000),
        ),
    ]