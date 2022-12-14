# Generated by Django 4.1.2 on 2022-10-10 17:12

import django.contrib.gis.db.models.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CoffeTypes',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, unique=True)),
                ('description', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Shop',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, unique=True)),
                ('street_name', models.CharField(max_length=50)),
                ('location', django.contrib.gis.db.models.fields.PointField(srid=4326)),
                ('type_of_coffe', models.ManyToManyField(to='resources.coffetypes')),
            ],
        ),
    ]
