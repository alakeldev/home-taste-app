from django.contrib import admin
from django.utils.html import format_html
from .models import Profile, Comment

# Register your models here.


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    """
    Customizes the admin panel interface for the Profile model.
    Set the filter on region field.
    """

    list_display = (
        "user",
        "name",
        "email",
        "phone_number",
        "cuisine_specialization",
        "Region",
        "country",
        "city",
        "created_on",
        "slug",
        "gender",
        "image",
        "facebook_link",
        "instagram_link",
        "youtube_link",
        "tiktok_link",
        "dish1",
        "dish2",
        "dish3",
        "dish4",
        "dish5",
        "formatted_instructions",
    )
    list_filter = ("Region",)

    def formatted_instructions(self, obj):
        """
        control instrunctions/schedules field
        to don't damage the view in admin panel if it's long.
        format_html to remove html tags
        """
        full_instructions = obj.instructions
        max_summary_length = 75

        if not full_instructions or len(full_instructions) == 0:
            return "-"
        summary = full_instructions[:max_summary_length]
        if len(full_instructions) > max_summary_length:
            summary += "..."
        return format_html(summary)

    formatted_instructions.short_description = "Instructions/Schedules"


@admin.register(Comment)
class ProfileAdmin(admin.ModelAdmin):
    """
    Customizes the admin panel interface for the comment model.
    Set the filter on is_approved field.
    """

    list_display = ("name", "comment", "email", "created_at", "is_approved")
    list_filter = ("is_approved",)
