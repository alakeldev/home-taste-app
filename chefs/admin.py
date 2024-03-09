from django.contrib import admin
from .models import Profile, Comment
from django.utils.html import format_html
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
        'formatted_instructions'
    )
    list_filter = ('Region',)

    # control instrunctions/schedules field to don't damage the view in admin panel if it's long
    # format_html to remove html tags
    def formatted_instructions(self, obj):
        full_instructions = obj.instructions
        max_summary_length = 75
        summary = full_instructions[:max_summary_length]
        if len(full_instructions) > max_summary_length:
            summary += "..."
        return format_html(summary)
    
    formatted_instructions.short_description = 'Instructions/Schedules'

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