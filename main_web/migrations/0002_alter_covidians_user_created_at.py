# Generated by Django 4.2.2 on 2023-06-11 17:49

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ("main_web", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="covidians",
            name="user_created_at",
            field=models.DateField(default=django.utils.timezone.now),
        ),
    ]