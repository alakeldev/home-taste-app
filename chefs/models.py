from django.db import models
from django.contrib.auth.models import User
from djrichtextfield.models import RichTextField
from django_resized import ResizedImageField
from django.db.models.signals import post_save
from django.utils.text import slugify
from phone_field import PhoneField

# Create your models here.

GENDER = (("F", "Female"), ("M", "Male"))

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
    name = models.CharField(max_length=30)
    email = models.EmailField(max_length=50, blank=True, null=True)
    phone_number = PhoneField(blank=True, help_text='Contact phone number')
    cuisine_specialization = models.CharField(max_length=50, default='-')
    Region = models.CharField(max_length=25, choices=REGION, default='Asia')
    country = models.CharField(max_length=25, default='-')
    city = models.CharField(max_length=25, default='-')
    created_on = models.DateTimeField(auto_now_add=True)
    slug = models.SlugField(blank=True, null=True)
    gender = models.CharField(choices = GENDER, blank=True, null=True)
    instructions = RichTextField(max_length = 20000, default='-')
    image = ResizedImageField(size=[400, None], quality=75, upload_to='profile/', force_format='WEBP', blank=True, null=True)
    facebook_link = models.URLField(blank=True, null=True)
    instagram_link = models.URLField(blank=True, null=True)
    youtube_link = models.URLField(blank=True, null=True)
    tiktok_link = models.URLField(blank=True, null=True)
    dish1 = ResizedImageField(size=[600, 600], quality=75, upload_to='dishes/', force_format='WEBP', blank=True, null=True)
    dish2 = ResizedImageField(size=[600, 600], quality=75, upload_to='dishes/', force_format='WEBP', blank=True, null=True)
    dish3 = ResizedImageField(size=[600, 600], quality=75, upload_to='dishes/', force_format='WEBP', blank=True, null=True)
    dish4 = ResizedImageField(size=[600, 600], quality=75, upload_to='dishes/', force_format='WEBP', blank=True, null=True)
    dish5 = ResizedImageField(size=[600, 600], quality=75, upload_to='dishes/', force_format='WEBP', blank=True, null=True)


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
    name = models.CharField(max_length=100)
    email = models.EmailField()
    comment = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    is_approved = models.BooleanField(default=False)

    def __str__(self):
        return f"Comment by {self.name} on {self.chef}"