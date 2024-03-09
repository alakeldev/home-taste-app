from django.contrib import admin
from .models import Profile, Comment
# Register your models here.

@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = (
        'user',
        'name',
        'email',
        'phone_number',
        'cuisine_specialization',
        'Region',
        'country',
        'city',
        'created_on',
        'slug',
        'gender',
        'image',
        'facebook_link',
        'instagram_link',
        'youtube_link',
        'tiktok_link',
        'dish1',
        'dish2',
        'dish3',
        'dish4',
        'dish5',
        'instructions'
    )
    list_filter = ('Region',)

@admin.register(Comment)
class ProfileAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'comment',
        'email',
        'created_at',
        'is_approved'
        )
    list_filter = ('is_approved',)