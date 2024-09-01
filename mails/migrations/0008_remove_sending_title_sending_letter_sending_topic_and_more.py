# Generated by Django 4.2.15 on 2024-08-30 19:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("mails", "0007_sending_company_sending_email_sending_title_and_more"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="sending",
            name="title",
        ),
        migrations.AddField(
            model_name="sending",
            name="letter",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="Письмо",
                to="mails.maill",
            ),
        ),
        migrations.AddField(
            model_name="sending",
            name="topic",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="Тема",
                to="mails.maill",
            ),
        ),
        migrations.AlterField(
            model_name="maill",
            name="body",
            field=models.TextField(verbose_name="Тело письма"),
        ),
    ]