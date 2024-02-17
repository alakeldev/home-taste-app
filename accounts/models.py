from django.db import models
from django.contrib.auth.models import User


# Create your models here.


class Profile(models.Model):

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=30)
    cuisine_specialization = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=30)
    created_on = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["-created_on"]

    def __str__(self):
        return f"Account: {self.name}"