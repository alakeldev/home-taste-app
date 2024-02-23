from django.shortcuts import render
from django.contrib.auth.models import User
from .models import Profile
from .forms import Login

# Create your views here.

def chefs(request):

    chefs_detail = User.objects.all()
    
    return render(request, 'account/chefs.html', {
        'chefs': chefs_detail,
    })


def chef_info(request, slug):

    chef_info = Profile.objects.get(slug = slug)

    return render(request, 'account/chef_info.html', {
    'chef_info': chef_info,
    })


def user_login(request):

    return render(request, 'account/login.html', {
    })