# Generated by Django 4.2.6 on 2023-10-14 13:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('posts_app', '0004_rename_notes_note'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='note',
            options={'ordering': ['-created_at']},
        ),
    ]