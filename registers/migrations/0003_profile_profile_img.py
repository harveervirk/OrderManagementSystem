# Generated by Django 3.0.8 on 2020-11-02 16:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('registers', '0002_auto_20200711_1208'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='profile_img',
            field=models.ImageField(default='default_profile.png', upload_to='Profile_images'),
        ),
    ]