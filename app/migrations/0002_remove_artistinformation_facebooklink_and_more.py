# Generated by Django 4.1.2 on 2023-05-02 14:40

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("app", "0001_initial"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="artistinformation",
            name="Facebooklink",
        ),
        migrations.RemoveField(
            model_name="artistinformation",
            name="Instalink",
        ),
        migrations.RemoveField(
            model_name="artistinformation",
            name="Twitterlink",
        ),
        migrations.CreateModel(
            name="Url",
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
                ("Instalink", models.URLField(null=True)),
                ("Facebooklink", models.URLField(null=True)),
                ("Twitterlink", models.URLField(null=True)),
                (
                    "user",
                    models.OneToOneField(
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
        ),
    ]
