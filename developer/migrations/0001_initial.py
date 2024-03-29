# Generated by Django 5.0.2 on 2024-03-08 08:06

from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Developer",
            fields=[
                (
                    "dev_id",
                    models.CharField(max_length=40, primary_key=True, serialize=False),
                ),
                ("password", models.CharField(max_length=20)),
                ("name", models.CharField(max_length=20)),
                ("manager", models.BooleanField(default=False)),
            ],
            options={
                "db_table": "developer",
            },
        ),
    ]
