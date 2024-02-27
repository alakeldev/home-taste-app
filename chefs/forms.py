from django import forms
from .models import Profile
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Submit


class UserProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['name','cuisine_specialization', 'Region', 'country', 'city', 'gender', 'instructions', 'image']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = 'post'
        self.helper.add_input(Submit('submit', 'Save Changes'))
