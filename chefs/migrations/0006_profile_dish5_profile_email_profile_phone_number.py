# Generated by Django 4.2.9 on 2024-03-02 16:45

from django.db import migrations, models
import django_resized.forms
import phone_field.models


class Migration(migrations.Migration):

    dependencies = [
        ('chefs', '0005_alter_profile_region_alter_profile_city_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='dish5',
            field=django_resized.forms.ResizedImageField(blank=True, crop=None, force_format='WEBP', keep_meta=True, null=True, quality=75, scale=None, size=[200, None], upload_to='dishes/'),
        ),
        migrations.AddField(
            model_name='profile',
            name='email',
            field=models.EmailField(default='-', max_length=50),
        ),
        migrations.AddField(
            model_name='profile',
            name='phone_number',
            field=phone_field.models.PhoneField(blank=True, help_text='Contact phone number', max_length=31),
        ),
    ]
