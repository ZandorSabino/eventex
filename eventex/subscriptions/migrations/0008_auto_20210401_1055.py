# Generated by Django 3.1.6 on 2021-04-01 13:55

from django.db import migrations, models
import eventex.subscriptions.validators
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('subscriptions', '0007_auto_20210329_2313'),
    ]

    operations = [
        migrations.AlterField(
            model_name='subscription',
            name='cpf',
            field=models.CharField(max_length=11, validators=[eventex.subscriptions.validators.validate_cpf], verbose_name='CPF'),
        ),
        migrations.AlterField(
            model_name='subscription',
            name='email',
            field=models.EmailField(blank=True, max_length=254, verbose_name='e-mail'),
        ),
        migrations.AlterField(
            model_name='subscription',
            name='phone',
            field=models.CharField(blank=True, max_length=20, verbose_name='telefone'),
        ),
        migrations.AlterField(
            model_name='subscription',
            name='uuid',
            field=models.UUIDField(default=uuid.UUID('1530245b-5ceb-4c7d-98dd-75362446e072'), editable=False, primary_key=True, serialize=False),
        ),
    ]
