# Generated by Django 3.2 on 2022-08-05 03:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("users", "0002_auto_20220804_1918"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="userlibrary",
            name="username",
        ),
    ]
