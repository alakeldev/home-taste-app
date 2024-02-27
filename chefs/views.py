from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import Profile
from .forms import UserProfileForm

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


@login_required(login_url='/accounts/login/')
def edit_profile(request):
    profile, created = Profile.objects.get_or_create(user=request.user)

    if request.method == 'POST':
        form = UserProfileForm(request.POST, request.FILES, instance=profile)
        if form.is_valid():
            form.save()
            return redirect('chefs:my_profile')
    else:
        form = UserProfileForm(instance=profile)

    return render(request, 'edit_profile.html', {'form': form})


@login_required
def delete_profile(request):
    if request.method == 'POST':
        user = request.user
        user.delete()
        messages.success(request, "Your profile has been deleted successfully.")
        return redirect('home') 
    return render(request, 'delete_profile.html')