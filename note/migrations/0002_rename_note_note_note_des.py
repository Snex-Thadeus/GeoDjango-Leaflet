# Generated by Django 4.1.2 on 2022-10-11 09:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('note', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='note',
            old_name='note',
            new_name='note_des',
        ),
    ]
