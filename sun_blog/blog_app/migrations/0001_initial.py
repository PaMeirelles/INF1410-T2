# Generated by Django 4.2.4 on 2023-11-09 15:02

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name="Post",
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
                ("titulo", models.CharField(max_length=250)),
                ("slug", models.SlugField(max_length=250)),
                ("corpo", models.TextField()),
                (
                    "dt_publicado",
                    models.DateTimeField(default=django.utils.timezone.now),
                ),
                ("dt_criado", models.DateTimeField(auto_now_add=True)),
                ("dt_atualizado", models.DateTimeField(auto_now=True)),
                (
                    "status",
                    models.CharField(
                        choices=[("DF", "Draft"), ("PB", "Published")],
                        default="DF",
                        max_length=2,
                    ),
                ),
                (
                    "autor",
                    models.ForeignKey(
                        default=0,
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="blog_posts",
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
            options={
                "ordering": ["-dt_publicado"],
                "indexes": [
                    models.Index(
                        fields=["-dt_publicado"], name="blog_app_po_dt_publ_111690_idx"
                    )
                ],
            },
        ),
    ]