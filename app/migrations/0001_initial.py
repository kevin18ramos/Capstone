# Generated by Django 4.1.2 on 2023-05-01 20:10

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name="Post",
            fields=[
                ("id", models.BigAutoField(primary_key=True, serialize=False)),
                (
                    "picture",
                    models.ImageField(blank=True, null=True, upload_to="images/"),
                ),
                ("name", models.CharField(max_length=200)),
                ("description", models.CharField(max_length=200)),
                ("date", models.DateField()),
                ("numOfArts", models.IntegerField(default=1)),
                ("price", models.DecimalField(decimal_places=2, max_digits=10)),
                ("stripe_product_id", models.CharField(max_length=100)),
                (
                    "user",
                    models.OneToOneField(
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="stripePrice",
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
                ("stripe_price_id", models.CharField(max_length=100)),
                ("price", models.IntegerField(default=0)),
                (
                    "product",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="app.post"
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="ArtistInformation",
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
                (
                    "profile_pic",
                    models.ImageField(
                        blank=True,
                        default="images/cabbage.jpg",
                        null=True,
                        upload_to="",
                    ),
                ),
                ("name", models.CharField(max_length=255, null=True)),
                ("firstname", models.CharField(max_length=200, null=True)),
                ("lastname", models.CharField(max_length=200, null=True)),
                ("email", models.CharField(max_length=200, null=True)),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("updated_at", models.DateTimeField(auto_now=True)),
                ("Instalink", models.URLField(null=True)),
                ("Facebooklink", models.URLField(null=True)),
                ("Twitterlink", models.URLField(null=True)),
                ("bio", models.TextField(blank=True, null=True)),
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
