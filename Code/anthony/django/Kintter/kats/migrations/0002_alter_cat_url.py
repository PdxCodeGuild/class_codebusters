# Generated by Django 3.2.5 on 2021-07-14 04:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('kats', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cat',
            name='url',
            field=models.URLField(unique=True),
        ),
    ]
