# Generated by Django 3.2.4 on 2021-06-29 22:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('yellowpages', '0002_rename_ed_ad'),
    ]

    operations = [
        migrations.AddField(
            model_name='ad',
            name='premium',
            field=models.BooleanField(default=False),
        ),
    ]
