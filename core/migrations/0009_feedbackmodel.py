
# Generated by Django 4.1.5 on 2023-01-24 10:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("core", "0008_productimagemodel_remove_productmodel_image_and_more"),
    ]

    operations = [
        migrations.CreateModel(
            name="FeedbackModel",
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
                ("name", models.CharField(max_length=255)),
                ("email", models.EmailField(max_length=16)),
                ("subject", models.CharField(max_length=255)),
                ("message", models.CharField(max_length=255)),
                ("is_replied", models.BooleanField(default=False)),
                ("status", models.BooleanField(default=False)),
                ("created_on", models.DateTimeField(auto_now_add=True)),
                ("updated_on", models.DateTimeField(auto_now=True)),
            ],
        ),
    ]