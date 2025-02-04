# Generated by Django 5.1.5 on 2025-01-30 05:13

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Category",
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
                (
                    "category_name",
                    models.CharField(
                        choices=[("men", "men"), ("women", "women")], max_length=255
                    ),
                ),
                ("category_description", models.TextField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name="Product",
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
                ("product_name", models.CharField(max_length=200)),
                ("product_description", models.TextField()),
                ("product_price", models.DecimalField(decimal_places=2, max_digits=10)),
                ("product_stock", models.IntegerField()),
                (
                    "product_image",
                    models.ImageField(blank=True, null=True, upload_to="media/"),
                ),
                ("product_added", models.DateTimeField(auto_now_add=True)),
                (
                    "product_category",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="products",
                        to="product.category",
                    ),
                ),
            ],
        ),
    ]
