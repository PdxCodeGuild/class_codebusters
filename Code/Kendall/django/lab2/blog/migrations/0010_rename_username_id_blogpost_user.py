# Generated by Django 3.2.4 on 2021-09-15 18:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0009_blogpost_username_id'),
    ]

    operations = [
        migrations.RenameField(
            model_name='blogpost',
            old_name='username_id',
            new_name='user',
        ),
    ]