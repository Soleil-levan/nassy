# Generated by Django 4.1.13 on 2023-12-17 00:38

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("compte", "0001_initial"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="utilisateur",
            options={"verbose_name": "user", "verbose_name_plural": "users"},
        ),
        migrations.RemoveConstraint(
            model_name="utilisateur",
            name="compte_utilisateur_unique",
        ),
    ]