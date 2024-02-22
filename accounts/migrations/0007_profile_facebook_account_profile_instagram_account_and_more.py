# Generated by Django 4.2.9 on 2024-02-22 20:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0006_profile_email'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='facebook_account',
            field=models.CharField(blank=True, max_length=80, null=True),
        ),
        migrations.AddField(
            model_name='profile',
            name='instagram_account',
            field=models.CharField(blank=True, max_length=80, null=True),
        ),
        migrations.AddField(
            model_name='profile',
            name='twitter_account',
            field=models.CharField(blank=True, max_length=80, null=True),
        ),
        migrations.AddField(
            model_name='profile',
            name='youtube_account',
            field=models.CharField(blank=True, max_length=80, null=True),
        ),
    ]
