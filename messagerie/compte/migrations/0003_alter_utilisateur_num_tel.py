# Generated by Django 4.1.13 on 2023-12-17 01:00

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("compte", "0002_alter_utilisateur_options_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="utilisateur",
            name="num_tel",
            field=models.CharField(blank=True, max_length=15),
        ),
    ]
