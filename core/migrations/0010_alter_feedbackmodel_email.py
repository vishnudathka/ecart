# Generated by Django 4.1.5 on 2023-01-24 10:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("core", "0009_feedbackmodel"),
    ]

    operations = [
        migrations.AlterField(
            model_name="feedbackmodel",
            name="email",
            field=models.EmailField(max_length=255),
        ),
    ]
