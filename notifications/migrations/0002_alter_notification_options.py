# Generated by Django 4.1.4 on 2023-01-03 21:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("notifications", "0001_initial"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="notification",
            options={"ordering": ["-timeModified"]},
        ),
    ]
