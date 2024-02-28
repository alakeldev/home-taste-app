from django.contrib import admin
from .models import Profile, Comment
# Register your models here.

@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = (
        'user',
        'name',
        'Region',
        'country',
        'cuisine_specialization',
        'city',
        'instructions',
        'gender',
        'image'
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