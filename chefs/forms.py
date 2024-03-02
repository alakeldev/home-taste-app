from django import forms
from .models import Profile, Comment
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Submit


class UserProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['name', 'image', 'email', 'phone_number','Region', 'country', 'city', 'gender','cuisine_specialization', 'instructions', 'facebook_link', 'instagram_link', 'tiktok_link', 'youtube_link', 'dish1', 'dish2','dish3','dish4','dish5',]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = 'post'
        self.helper.add_input(Submit('submit', 'Save Changes'))


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['name', 'email', 'comment']