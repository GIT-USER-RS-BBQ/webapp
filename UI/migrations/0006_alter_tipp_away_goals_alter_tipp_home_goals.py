# Generated by Django 5.0.6 on 2024-06-12 13:44

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("UI", "0005_tournament_groupe_tournament_match_tournament"),
    ]

    operations = [
        migrations.AlterField(
            model_name="tipp",
            name="away_goals",
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name="tipp",
            name="home_goals",
            field=models.IntegerField(null=True),
        ),
    ]