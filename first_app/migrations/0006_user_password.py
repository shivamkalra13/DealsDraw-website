# Generated by Django 2.1.4 on 2020-04-17 11:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('first_app', '0005_auto_20200417_1700'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='password',
            field=models.CharField(default='no', max_length=32),
        ),
    ]
