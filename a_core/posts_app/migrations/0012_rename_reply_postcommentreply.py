# Generated by Django 4.2.6 on 2023-10-21 17:39

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('posts_app', '0011_alter_comment_options_reply'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Reply',
            new_name='PostCommentReply',
        ),
    ]
