# Generated by Django 2.1.4 on 2020-04-17 11:30

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('first_app', '0004_auto_20200417_1651'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='phone',
            field=models.BigIntegerField(primary_key=True, serialize=False, validators=[django.core.validators.RegexValidator(message='Length has to be 10', regex='^[0-9]{10}$')]),
        ),
    ]
