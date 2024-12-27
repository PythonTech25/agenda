# Generated by Django 5.1.4 on 2024-12-27 22:26

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Contact",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("firstname", models.CharField(max_length=80)),
                ("lastname", models.CharField(max_length=80)),
                ("phone", models.CharField(max_length=14)),
                ("email", models.EmailField(max_length=80)),
                (
                    "create_date",
                    models.DateTimeField(default=django.utils.timezone.now),
                ),
                ("description", models.TextField(blank=True)),
            ],
        ),
    ]
