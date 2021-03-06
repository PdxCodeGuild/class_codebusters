# Generated by Django 3.2.4 on 2021-08-05 02:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Level',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('evolution', models.CharField(max_length=15)),
            ],
        ),
        migrations.CreateModel(
            name='Digimon',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=15)),
                ('img', models.URLField()),
                ('level', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='digimon', to='api.level')),
            ],
        ),
    ]
