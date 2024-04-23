# Generated by Django 5.0.2 on 2024-04-23 09:06

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("CMS", "0010_alter_inventory_options"),
    ]

    operations = [
        migrations.AddField(
            model_name="inventory",
            name="record",
            field=models.AutoField(default=1, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name="inventory",
            name="product_id",
            field=models.OneToOneField(
                db_column="product_id",
                on_delete=django.db.models.deletion.PROTECT,
                to="CMS.product",
                verbose_name="product",
            ),
        ),
    ]