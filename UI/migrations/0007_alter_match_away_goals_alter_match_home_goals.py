# Generated by Django 5.0.6 on 2024-06-12 21:52

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("UI", "0006_alter_tipp_away_goals_alter_tipp_home_goals"),
    ]

    operations = [
        migrations.AlterField(
            model_name="match",
            name="away_goals",
            field=models.IntegerField(default=None, null=True),
        ),
        migrations.AlterField(
            model_name="match",
            name="home_goals",
            field=models.IntegerField(default=None, null=True),
        ),
    ]