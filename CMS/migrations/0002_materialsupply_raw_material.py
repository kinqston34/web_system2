# Generated by Django 5.0.2 on 2024-04-11 10:31

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("CMS", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="MaterialSupply",
            fields=[
                (
                    "supplier_id",
                    models.CharField(max_length=7, primary_key=True, serialize=False),
                ),
                ("name", models.CharField(max_length=40)),
                ("address", models.CharField(max_length=50)),
                ("tel", models.CharField(max_length=9)),
                ("salesman", models.CharField(max_length=10)),
                ("salesman_phone", models.CharField(max_length=10)),
            ],
            options={
                "db_table": "Material_Supply",
            },
        ),
        migrations.CreateModel(
            name="Raw_Material",
            fields=[
                (
                    "material_id",
                    models.CharField(max_length=8, primary_key=True, serialize=False),
                ),
                ("name", models.CharField(max_length=30)),
                ("category", models.CharField(max_length=2)),
                (
                    "supplier_id",
                    models.ForeignKey(
                        db_column="supplier_id",
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="material_supplies",
                        to="CMS.materialsupply",
                    ),
                ),
            ],
            options={
                "db_table": "Raw_Material",
            },
        ),
    ]
