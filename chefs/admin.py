from django.contrib import admin
from .models import Profile
# Register your models here.

@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = (
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