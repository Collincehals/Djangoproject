# Generated by Django 4.2.6 on 2023-10-16 16:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('a_users', '0002_rename_fullname_profile_realname'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='image',
            field=models.ImageField(blank=True, default='profilepics/City_lights_wit_0.png', null=True, upload_to='profilepics/'),
        ),
    ]