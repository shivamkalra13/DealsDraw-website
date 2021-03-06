# Generated by Django 2.1.4 on 2020-04-16 17:13

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Offer',
            fields=[
                ('oid', models.CharField(max_length=10, primary_key=True, serialize=False)),
                ('category', models.CharField(max_length=20)),
                ('cashback', models.PositiveIntegerField()),
                ('link', models.URLField()),
                ('title', models.CharField(max_length=50)),
                ('terms', models.CharField(max_length=300)),
            ],
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('oid', models.CharField(max_length=10, primary_key=True, serialize=False)),
                ('date', models.DateField(auto_now_add=True)),
                ('amount', models.PositiveIntegerField()),
                ('cashback', models.PositiveIntegerField()),
                ('status', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('pid', models.CharField(max_length=10, primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=50)),
                ('price', models.PositiveIntegerField()),
                ('discount', models.PositiveIntegerField()),
                ('cashback', models.PositiveIntegerField()),
                ('rating', models.PositiveIntegerField()),
                ('specs', models.CharField(max_length=300)),
                ('link', models.URLField()),
            ],
        ),
        migrations.CreateModel(
            name='Referal',
            fields=[
                ('refid', models.CharField(max_length=10, primary_key=True, serialize=False)),
                ('date', models.DateField(auto_now_add=True)),
                ('status', models.CharField(max_length=20)),
                ('reward', models.PositiveIntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Store',
            fields=[
                ('name', models.CharField(max_length=10, primary_key=True, serialize=False)),
                ('total_orders', models.PositiveIntegerField(default=0)),
                ('payment_threshold_period', models.PositiveIntegerField(blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('phone', models.PositiveIntegerField(primary_key=True, serialize=False, validators=[django.core.validators.RegexValidator(message='Length has to be 10', regex='^.{10}$')])),
                ('name', models.CharField(max_length=50)),
                ('email', models.EmailField(blank=True, max_length=200)),
                ('earning', models.PositiveIntegerField(default=0)),
            ],
        ),
        migrations.AddField(
            model_name='referal',
            name='user1',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='user1', to='first_app.User'),
        ),
        migrations.AddField(
            model_name='referal',
            name='user2',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='user2', to='first_app.User'),
        ),
        migrations.AddField(
            model_name='order',
            name='product',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='first_app.Product'),
        ),
        migrations.AddField(
            model_name='order',
            name='store',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='first_app.Store'),
        ),
        migrations.AddField(
            model_name='order',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='first_app.User'),
        ),
        migrations.AddField(
            model_name='offer',
            name='store',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='first_app.Store'),
        ),
    ]
