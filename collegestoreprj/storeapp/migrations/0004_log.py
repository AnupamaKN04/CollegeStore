# Generated by Django 4.2.1 on 2023-05-22 08:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("storeapp", "0003_rename_category_product_department_and_more"),
    ]

    operations = [
        migrations.CreateModel(
            name="Log",
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
                ("name", models.CharField(blank=True, max_length=100)),
                ("password", models.CharField(blank=True, max_length=100)),
            ],
        ),
    ]
