# Generated by Django 5.0.2 on 2024-04-22 12:16

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("CMS", "0005_product_stage"),
    ]

    operations = [
        migrations.AlterField(
            model_name="product",
            name="stage",
            field=models.CharField(max_length=3),
        ),
    ]
