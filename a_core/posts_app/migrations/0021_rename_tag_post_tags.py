# Generated by Django 4.2.6 on 2023-11-09 22:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('posts_app', '0020_tag_post_tag'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post',
            old_name='tag',
            new_name='tags',
        ),
    ]