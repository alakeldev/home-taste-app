from django.db import models
from django.contrib.auth.models import User
from djrichtextfield.models import RichTextField
from django_resized import ResizedImageField
from django.db.models.signals import post_save
from django.utils.text import slugify

# Create your models here.

GENDER = (("Female", "Female"), ("Male", "Male"))

REGION = (
    ("Africa", "Africa"),
    ("Asia", "Asia"),
    ("Caribbean", "Caribbean"),
    ("Central America", "Central America"),
    ("Europe", "Europe"),
    ("North America", "North America"),
    ("Oceania", "Oceania"),
    ("South America", "South America"),
)

class Profile(models.Model):

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(("Name"), max_length=20, help_text='You can enter a different name from your username.')
    image = ResizedImageField(("Profile Picture"), size=[400, None], quality=75, upload_to='profile/', force_format='WEBP', blank=True, null=True, help_text='Please upload your profile picture.')
    email = models.EmailField(("Contact Email"), max_length=50, blank=True, null=True, help_text='You can enter a different email from the one used during registration.')
    phone_number = models.CharField(("Phone Number"), max_length=25, blank=True, null=True, help_text='Please provide your contact phone/mobile number.')
    cuisine_specialization = models.CharField(("Cuisine Type"), max_length=25, blank=True, null=True, help_text='Specify your cuisine & culinary expertise (e.g., Indian, Syrian, Italian).')
    Region = models.CharField(("Region"), choices=REGION, default='Europe', help_text='Please specify your region.')
    country = models.CharField(("Country"), max_length=12, blank=True, null=True, help_text='Please enter your country of residence (use abbreviations if its long).')
    city = models.CharField(("City"), max_length=12, blank=True, null=True, help_text='Please enter your city of residence (use abbreviations if its long).')
    created_on = models.DateTimeField(auto_now_add=True)
    slug = models.SlugField(blank=True, null=True)
    gender = models.CharField(choices = GENDER, blank=True, null=True, help_text='Please specify your gender.')
    instructions = RichTextField(("Please Share Below Your Instructions/Cook Schedules"), max_length=20000, blank=True, null=True)
    facebook_link = models.URLField(("Facebook URL"), blank=True, null=True, help_text='Please enter the URL of your Facebook account.')
    instagram_link = models.URLField(("Instagram URL"), blank=True, null=True, help_text='Please enter the URL of your Instagram account.')
    youtube_link = models.URLField(("Youtube URL"), blank=True, null=True, help_text='Please enter the URL of your Youtube channel.')
    tiktok_link = models.URLField(("Tiktok URL"), blank=True, null=True, help_text='Please enter the URL of your Tiktok account.')
    dish1 = ResizedImageField(("Dish Image-1"), size=[600, 600], quality=75, upload_to='dishes/', force_format='WEBP', blank=True, null=True, help_text='Please upload a photo of your culinary masterpiece')
    dish2 = ResizedImageField(("Dish Image-2"), size=[600, 600], quality=75, upload_to='dishes/', force_format='WEBP', blank=True, null=True, help_text='Please upload a photo of your culinary masterpiece')
    dish3 = ResizedImageField(("Dish Image-3"), size=[600, 600], quality=75, upload_to='dishes/', force_format='WEBP', blank=True, null=True, help_text='Please upload a photo of your culinary masterpiece')
    dish4 = ResizedImageField(("Dish Image-4"), size=[600, 600], quality=75, upload_to='dishes/', force_format='WEBP', blank=True, null=True, help_text='Please upload a photo of your culinary masterpiece')
    dish5 = ResizedImageField(("Dish Image-5"), size=[600, 600], quality=75, upload_to='dishes/', force_format='WEBP', blank=True, null=True, help_text='Please upload a photo of your culinary masterpiece')


    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.user.username)
        super(Profile, self).save(*args, **kwargs)

    class Meta:
        ordering = ['-created_on']

    def __str__(self):
        return '%s' %(self.user.username)
    

def create_profile(sender, **kwargs):
    if kwargs['created']:
        Profile.objects.create(user=kwargs['instance'])

post_save.connect(create_profile, sender=User)


class Comment(models.Model):
    chef = models.ForeignKey(Profile, on_delete=models.CASCADE)
    name = models.CharField(max_length=20, help_text='Please Enter Your Name.')
    email = models.EmailField(max_length=50, help_text='Please Enter Your Email.')
    comment = models.TextField(max_length=200, help_text='Please Enter Your Comment.')
    created_at = models.DateTimeField(auto_now_add=True)
    is_approved = models.BooleanField(default=False)

    def __str__(self):
        return f"Comment by {self.name} on {self.chef}"