# Generated by Django 4.1.2 on 2022-10-11 09:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('note', '0002_rename_note_note_note_des'),
    ]

    operations = [
        migrations.RenameField(
            model_name='note',
            old_name='note_des',
            new_name='note',
        ),
    ]