# Generated by Django 5.1.5 on 2025-01-30 05:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("product", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="category",
            name="category_name",
            field=models.CharField(
                choices=[("men", "men"), ("women", "women")],
                max_length=255,
                unique=True,
            ),
        ),
    ]
