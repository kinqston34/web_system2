# Generated by Django 5.0.2 on 2024-04-22 13:35

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("CMS", "0007_inventory"),
    ]

    operations = [
        migrations.AlterField(
            model_name="inventory",
            name="product_id",
            field=models.OneToOneField(
                db_column="product_id",
                on_delete=django.db.models.deletion.PROTECT,
                primary_key=True,
                serialize=False,
                to="CMS.product",
                verbose_name="product",
            ),
        ),
    ]
