# Generated by Django 4.2.7 on 2023-11-30 07:04

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Strategy',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('is_initialized', models.BooleanField(default=False)),
                ('is_running', models.BooleanField(default=False)),
                ('parameters', models.JSONField()),
            ],
        ),
    ]
