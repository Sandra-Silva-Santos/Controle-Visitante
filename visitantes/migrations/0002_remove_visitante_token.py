# Generated by Django 4.1.5 on 2023-02-04 01:52

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("visitantes", "0001_initial"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="visitante",
            name="token",
        ),
    ]
