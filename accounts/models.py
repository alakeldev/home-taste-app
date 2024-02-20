from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save

# Create your models here.


class Profile(models.Model):

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=30)
    cuisine_specialization = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=30)
    created_on = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(upload_to='profile', default='profile/default.jpg')

    class Meta:
        ordering = ["-created_on"]

    def __str__(self):
        return f"User: {self.user} | Name: {self.name}"
    



def create_profile(sender , **kwargs):
    if kwargs['created']:
        Profile.objects.create(user=kwargs['instance'])


post_save.connect(create_profile, sender=User)