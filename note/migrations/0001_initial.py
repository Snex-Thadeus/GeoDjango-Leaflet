# Generated by Django 4.1.2 on 2022-10-11 09:00

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Note',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('note_heading', models.CharField(blank=True, max_length=200, null=True)),
                ('note', models.CharField(blank=True, max_length=1000, null=True)),
                ('lat', models.FloatField()),
                ('lng', models.FloatField()),
            ],
        ),
    ]
