from django.shortcuts import render
from django.contrib.auth.models import User
from .models import Profile
# Create your views here.


def chefs_list(request):
    chefs = User.objects.all()
    return render(request, 'chefs.html', {
        'chefs' : chefs,
    })


def chef_info(request, slug):
    chef_info = Profile.objects.get(slug=slug)

    return render(request, 'chef_info.html', {
        'chef_info' : chef_info
    })