# Generated by Django 4.1.5 on 2023-02-04 20:39

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("visitantes", "0002_remove_visitante_token"),
    ]

    operations = [
        migrations.AddField(
            model_name="visitante",
            name="token",
            field=models.CharField(
                default="", editable=False, max_length=8, unique=True
            ),
        ),
    ]
