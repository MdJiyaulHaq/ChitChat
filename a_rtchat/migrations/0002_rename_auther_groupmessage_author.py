# Generated by Django 5.1.6 on 2025-02-22 12:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('a_rtchat', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='groupmessage',
            old_name='auther',
            new_name='author',
        ),
    ]
