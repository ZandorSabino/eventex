# Generated by Django 3.1.6 on 2021-03-30 02:04

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('subscriptions', '0007_auto_20210329_2254'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='subscription',
            name='id',
        ),
        migrations.AddField(
            model_name='subscription',
            name='uuid',
            field=models.UUIDField(default=uuid.UUID('b8afd4e6-0003-44d7-8f5e-18c640ea7a04'), editable=False, primary_key=True, serialize=False),
        ),
    ]
