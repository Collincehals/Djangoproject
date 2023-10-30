# Generated by Django 4.2.6 on 2023-10-30 15:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts_app', '0015_postcomment_likes_postcommentreply_likes'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='artist',
        ),
        migrations.AlterField(
            model_name='post',
            name='image',
            field=models.ImageField(upload_to='postimages/'),
        ),
        migrations.AlterField(
            model_name='post',
            name='url',
            field=models.URLField(blank=True, null=True),
        ),
    ]
