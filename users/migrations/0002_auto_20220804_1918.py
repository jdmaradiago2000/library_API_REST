# Generated by Django 3.2 on 2022-08-05 00:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("users", "0001_initial"),
    ]

    operations = [
        migrations.AlterModelManagers(
            name="userlibrary",
            managers=[],
        ),
        migrations.AlterField(
            model_name="userlibrary",
            name="email",
            field=models.EmailField(
                max_length=254, unique=True, verbose_name="email address"
            ),
        ),
    ]
