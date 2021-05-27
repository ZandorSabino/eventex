# Generated by Django 3.1.6 on 2021-05-27 23:42

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('subscriptions', '0019_auto_20210407_1210'),
    ]

    operations = [
        migrations.AlterField(
            model_name='subscription',
            name='uuid',
            field=models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False),
        ),
    ]
