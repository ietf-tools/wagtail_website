# Generated by Django 3.2.13 on 2023-05-24 00:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('utils', '0006_textchunk'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='socialmediasettings',
            name='default_sharing_image',
        ),
        migrations.RemoveField(
            model_name='socialmediasettings',
            name='default_sharing_text',
        ),
        migrations.RemoveField(
            model_name='socialmediasettings',
            name='facebook_app_id',
        ),
        migrations.RemoveField(
            model_name='socialmediasettings',
            name='site_name',
        ),
        migrations.RemoveField(
            model_name='socialmediasettings',
            name='twitter_handle',
        ),
        migrations.AddField(
            model_name='socialmediasettings',
            name='linkedin',
            field=models.CharField(blank='True', help_text='Link to linkedin profile', max_length=255),
        ),
        migrations.AddField(
            model_name='socialmediasettings',
            name='mastodon',
            field=models.CharField(blank='True', help_text='Link to mastodon profile', max_length=255),
        ),
        migrations.AddField(
            model_name='socialmediasettings',
            name='twitter',
            field=models.CharField(blank='True', help_text='Link to twitter profile', max_length=255),
        ),
        migrations.AddField(
            model_name='socialmediasettings',
            name='youtube',
            field=models.CharField(blank='True', help_text='Link to youtube account', max_length=255),
        ),
    ]