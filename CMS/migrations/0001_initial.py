# Generated by Django 5.0.2 on 2024-04-10 11:55

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        ("HRM", "0006_remove_hr_level"),
    ]

    operations = [
        migrations.CreateModel(
            name="CMS",
            fields=[
                (
                    "CMS_id",
                    models.ForeignKey(
                        db_column="CMS_id",
                        limit_choices_to={"developments": "ED"},
                        on_delete=django.db.models.deletion.CASCADE,
                        primary_key=True,
                        related_name="CMS_id",
                        serialize=False,
                        to="HRM.staff",
                    ),
                ),
                ("password", models.CharField(max_length=20)),
            ],
            options={
                "db_table": "CMS",
            },
        ),
    ]
