from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import Profile, Comment
from .forms import UserProfileForm
from .forms import CommentForm
from django.db.models import Q

# Create your views here.

def chefs_list(request):
    search_query = request.GET.get('search', '')
    queryset = User.objects.all()
    if search_query:
        queryset = queryset.filter(
            Q(profile__Region__icontains=search_query) | 
            Q(profile__country__icontains=search_query) | 
            Q(profile__city__icontains=search_query) 
        )
    return render(request, 'chefs.html', {
        'chefs': queryset,
    })


def chef_info(request, slug):
    chef_info = get_object_or_404(Profile, slug=slug)
    comments = Comment.objects.filter(chef=chef_info, is_approved=True)
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.chef = chef_info
            comment.save()
            return redirect(request.path)
    else:
        form = CommentForm()
    return render(request, 'chef_info.html', {
        'chef_info' : chef_info, 'comments': comments, 'form': form
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


@login_required(login_url='/accounts/login/')
def delete_profile(request):
    if request.method == 'POST':
        user = request.user
        user.delete()
        messages.success(request, "Your profile has been deleted successfully.")
        return redirect('home') 
    return render(request, 'delete_profile.html')