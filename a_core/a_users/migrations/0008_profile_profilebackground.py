# Generated by Django 4.2.7 on 2023-12-09 15:16

from django.db import migrations
import django_resized.forms


class Migration(migrations.Migration):

    dependencies = [
        ('a_users', '0007_profile_followers'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='profilebackground',
            field=django_resized.forms.ResizedImageField(blank=True, crop=None, force_format=None, keep_meta=True, null=True, quality=70, scale=None, size=[1920, 1080], upload_to='profilepics/'),
        ),
    ]