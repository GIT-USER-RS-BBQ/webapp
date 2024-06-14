# Generated by Django 5.0.6 on 2024-06-11 09:02

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("UI", "0002_match_match_type"),
    ]

    operations = [
        migrations.AlterField(
            model_name="match",
            name="match_type",
            field=models.CharField(
                choices=[
                    ("PRELIMENARY", "prelimenary"),
                    ("FINALS_8", "finals_8"),
                    ("FINALS_4", "finals_4"),
                    ("FINALS_2", "finals_2"),
                    ("FINAL", "final"),
                ],
                max_length=11,
                null=True,
            ),
        ),
    ]