# Generated by Django 3.2.6 on 2021-08-20 13:03

from django.conf import settings
import django.contrib.auth.models
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("newsboard", "0002_auto_20210820_1430"),
    ]

    operations = [
        migrations.CreateModel(
            name="Voted",
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
                ("voted", models.BooleanField(default=False)),
                (
                    "post_voted",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="newsboard.post"
                    ),
                ),
                (
                    "user_voted",
                    models.ForeignKey(
                        default=django.contrib.auth.models.User,
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
        ),
    ]