from django.db import models
from django.contrib.auth.models import User

from djrichtextfield.models import RichTextField
from django_resized import ResizedImageField
from django.db.models.signals import post_save

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
    name = models.CharField(max_length=100)
    cuisine_specialization = models.CharField(max_length=150, default='Indian, Syrian, Italian...' ,blank=True, null=True)
    Region = models.CharField(max_length=50, choices=REGION, default='Europe')
    country = models.CharField(max_length=25, blank=True, null=True)
    city = models.CharField(max_length=25, blank=True, null=True)
    created_on = models.DateTimeField(auto_now_add=True)
    slug = models.SlugField(blank=True, null=True)
    gender = models.CharField(choices = GENDER, blank=True, null=True, default='not specify')
    instructions = RichTextField(max_length = 20000, blank=True, null=True)
    image = ResizedImageField(size=[200, None], quality=75, upload_to='profile/', force_format='WEBP', blank=True, null=True)


    class Meta:
        ordering = ['-created_on']

    def __str__(self):
        return '%s' %(self.user.username)
    

def create_profile(sender, **kwargs):
    if kwargs['created']:
        Profile.objects.create(user=kwargs['instance'])

post_save.connect(create_profile, sender=User)