# Generated by Django 4.2.7 on 2023-11-28 10:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts_app', '0024_alter_post_author'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='note',
            name='author',
        ),
        migrations.RemoveField(
            model_name='note',
            name='likes',
        ),
        migrations.RemoveField(
            model_name='post',
            name='image',
        ),
        migrations.AddField(
            model_name='post',
            name='media',
            field=models.FileField(blank=True, null=True, upload_to=''),
        ),
        migrations.AlterField(
            model_name='post',
            name='tags',
            field=models.ManyToManyField(blank=True, null=True, to='posts_app.tag'),
        ),
        migrations.DeleteModel(
            name='LikedNote',
        ),
        migrations.DeleteModel(
            name='Note',
        ),
    ]
