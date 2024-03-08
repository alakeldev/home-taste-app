from django import forms
from .models import Profile, Comment
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit


class UserProfileForm(forms.ModelForm):

    class Meta:
        model = Profile
        fields = ['name', 'image', 'email', 'phone_number','Region', 'country', 'city', 'gender','cuisine_specialization', 'instructions', 'facebook_link', 'instagram_link', 'tiktok_link', 'youtube_link', 'dish1', 'dish2','dish3','dish4','dish5',]

    def clean(self):
        cleaned_data = super().clean()
        name = cleaned_data.get('name')
        city = cleaned_data.get('city')
        country = cleaned_data.get('country')
        cuisine = cleaned_data.get('cuisine_specialization')
        phone_number = cleaned_data.get('phone_number')
        email = cleaned_data.get('email')
        url_fields = ['facebook_link', 'instagram_link', 'youtube_link', 'tiktok_link']

        valid_characters1 = set("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ ")
        valid_characters2 = set("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ,-/ ")
        valid_characters3 = set("0123456789 -()+")

        if name and not all(char in valid_characters1 for char in name):
            self.add_error('name', "Name should contain only letters.")

        if city and not all(char in valid_characters1 for char in city):
            self.add_error('city', "City should contain only letters.")

        if country and not all(char in valid_characters1 for char in country):
            self.add_error('country', "Country should contain only letters.")

        if cuisine and not all(char in valid_characters2 for char in cuisine):
            self.add_error('cuisine_specialization', "Cuisine Type should contain only letters, (,), (-), and (/).")

        if phone_number and not all(char in valid_characters3 for char in phone_number):
            self.add_error('phone_number', "Phone Number should contain only digits, (-), (+) and ().")

        if email:
            email_validator = forms.EmailValidator()
            try:
                email_validator(email)
            except forms.ValidationError:
                self.add_error('email', "Invalid Email address!.")

        for field_name in url_fields:
            field_value = cleaned_data.get(field_name)
            if field_value:
                platform_name = field_name.split('_')[0]
                if platform_name not in field_value.lower():
                    self.add_error(field_name, f"Invalid {platform_name.capitalize()} URL.")

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = 'post'
        self.helper.add_input(Submit('submit', 'Save Changes'))


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['name', 'email', 'comment']