# Generated by Django 4.2.15 on 2024-08-31 01:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("blog", "0001_initial"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="blog",
            options={"verbose_name": "Статья", "verbose_name_plural": "Статьи"},
        ),
    ]