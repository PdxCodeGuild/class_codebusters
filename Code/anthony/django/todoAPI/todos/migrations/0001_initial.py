# Generated by Django 3.2.5 on 2021-08-03 02:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='TodoPriority',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.CharField(max_length=20)),
                ('value', models.IntegerField(default=3)),
            ],
        ),
        migrations.CreateModel(
            name='TodoItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.CharField(max_length=200)),
                ('created_date', models.DateField(auto_now_add=True)),
                ('completed_date', models.DateField(blank=True, null=True)),
                ('priority', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='todos.todopriority')),
            ],
        ),
    ]
