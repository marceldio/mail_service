# Generated by Django 4.2.15 on 2024-08-28 21:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Maill",
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
                ("title", models.CharField(max_length=100, verbose_name="Заголовок")),
                ("body", models.TextField(verbose_name="Содержание")),
                (
                    "recipient",
                    models.EmailField(max_length=254, verbose_name="Адресат"),
                ),
                ("sent", models.BooleanField(default=False)),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("updated_at", models.DateTimeField(auto_now=True)),
            ],
            options={
                "verbose_name": "Письмо",
                "verbose_name_plural": "Письма",
                "ordering": ["title", "recipient", "updated_at", "created_at", "sent"],
            },
        ),
        migrations.CreateModel(
            name="Recipient",
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
                ("first_name", models.CharField(max_length=100, verbose_name="Имя")),
                (
                    "last_name",
                    models.CharField(
                        blank=True, max_length=100, null=True, verbose_name="Фамилия"
                    ),
                ),
                (
                    "middle_name",
                    models.CharField(
                        blank=True, max_length=100, null=True, verbose_name="Отчество"
                    ),
                ),
                ("email", models.EmailField(max_length=254, verbose_name="Email")),
                (
                    "comment",
                    models.TextField(blank=True, null=True, verbose_name="Комментарий"),
                ),
                (
                    "maill",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        related_name="maills",
                        to="mails.maill",
                        verbose_name="Письмо",
                    ),
                ),
            ],
            options={
                "verbose_name": "Адресат",
                "verbose_name_plural": "Адресаты",
                "ordering": ["first_name", "last_name", "email", "comment"],
            },
        ),
    ]