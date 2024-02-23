from django.shortcuts import render , redirect
from django.contrib.auth.models import User
from .models import Profile
from .forms import Login
from django.contrib.auth import authenticate , login

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
    if request.method == 'POST':
        form = Login()
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username , password=password)
        if user is not None:
            login(request , user)
            return redirect('accounts:chefs_accounts')
    else:
        form = Login()
    return render(request, 'account/login.html', {
        'form': form
    })