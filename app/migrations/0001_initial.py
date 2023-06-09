# Generated by Django 4.1.2 on 2023-04-27 19:56

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
            name="Cart",
            fields=[
                ("id", models.BigAutoField(primary_key=True, serialize=False)),
                (
                    "amount",
                    models.DecimalField(decimal_places=2, default=0, max_digits=10),
                ),
                (
                    "customer_email",
                    models.EmailField(default="default@gmail.com", max_length=254),
                ),
                ("stripe_payment_intent", models.CharField(max_length=200)),
                ("has_paid", models.BooleanField(default=False)),
                (
                    "product",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.PROTECT, to="app.post"
                    ),
                ),
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
                ("websiteLink", models.URLField(null=True)),
                ("bio", models.TextField(blank=True, null=True)),
                ("cart", models.CharField(max_length=200, null=True)),
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
