# Generated by Django 3.2.4 on 2021-09-15 17:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0005_blogpost_user'),
    ]

    operations = [
        migrations.RenameField(
            model_name='blogpost',
            old_name='user',
            new_name='username',
        ),
    ]