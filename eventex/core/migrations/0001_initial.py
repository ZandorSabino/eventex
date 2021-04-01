# Generated by Django 3.1.6 on 2021-04-01 17:20

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Speaker',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('slug', models.SlugField()),
                ('website', models.URLField()),
                ('photo', models.URLField()),
                ('description', models.TextField()),
            ],
        ),
    ]
