# Generated by Django 3.1.6 on 2021-04-07 14:38

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ("subscriptions", "0015_auto_20210407_1116"),
    ]

    operations = [
        migrations.AlterField(
            model_name="subscription",
            name="uuid",
            field=models.UUIDField(
                default=uuid.UUID("c4f7d9cd-c8df-4614-a102-cff3e9f2ee24"),
                editable=False,
                primary_key=True,
                serialize=False,
            ),
        ),
    ]
