# Generated by Django 4.2.17 on 2025-01-28 10:54

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="ServerStatus",
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
                ("timestamp", models.DateTimeField(auto_now_add=True)),
                ("cpu_usage", models.FloatField()),
                ("memory_usage", models.FloatField()),
                ("disk_usage", models.FloatField()),
            ],
        ),
    ]
