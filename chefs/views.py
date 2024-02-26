from django.shortcuts import render
from django.contrib.auth.models import User
from .models import Profile
from django.contrib.auth.decorators import login_required
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

@login_required(login_url='/accounts/login/')
def my_profile(request):
    return render(request, 'my_profile.html', {
        'my_profile' : my_profile
    })