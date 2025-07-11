from django.db import migrations, models
import os

class Migration(migrations.Migration):

    dependencies = [
        ("myapp", "0002_alter_hradmin_email"),
    ]

    operations = [
        migrations.CreateModel(
            name="Employee",
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
                ("name", models.CharField(max_length=100)),
                ("email", models.EmailField(max_length=100, unique=True)),
                ("department", models.CharField(max_length=100)),
                ("designation", models.CharField(max_length=100)),
                ("join_date", models.DateField()),
            ],
        ),
    ]
