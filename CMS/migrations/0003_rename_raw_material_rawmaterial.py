# Generated by Django 5.0.2 on 2024-04-11 12:24

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("CMS", "0002_materialsupply_raw_material"),
    ]

    operations = [
        migrations.RenameModel(
            old_name="Raw_Material",
            new_name="RawMaterial",
        ),
    ]
