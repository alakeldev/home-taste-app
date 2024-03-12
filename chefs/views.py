from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.db.models import Q
from .models import Profile, Comment
from .forms import UserProfileForm
from .forms import CommentForm

# Create your views here.


def chefs_list(request):
    """
    Retrieves a list of chefs cards based on search criteria.
    If chefs are found, renders the 'chefs.html' template with 
    the context = chefs cards.
    Otherwise, displays a message indicating no match.

    """
    search_query = request.GET.get('search', '')
    queryset = User.objects.all()
    if search_query:
        queryset = queryset.filter(
            Q(profile__Region__icontains=search_query) | 
            Q(profile__country__icontains=search_query) | 
            Q(profile__city__icontains=search_query) 
        )
    if not queryset:
        context = {'message': 'Sorry! no match found.'}
    else:
        context = {'chefs': queryset}
    return render(request, 'chefs.html', context)


def chef_info(request, slug):
    """
    Retrieves information about a chef based on the provided slug.
    If the request method is POST:
        - Validates and saves a new comment related to the chef.
        - Displays a success message if the comment is submitted successfully.
        - Redirects back to the same page.
        - If the comment submission fails, displays an error message.
    If the request method is not POST:
        - Initializes an empty comment form.
        - Retrieves the chef's profile information and approved comments.
        - Renders the 'chef_info.html' template with relevant context.
    """

    chef_info = get_object_or_404(Profile, slug=slug)
    comments = Comment.objects.filter(chef=chef_info, is_approved=True)
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.chef = chef_info
            comment.save()
            messages.success(request, 'Your comment has been submitted successfully.')
            return redirect(request.path)
        else:
            messages.error(request, 'Your comment submission has failed!.')
            return render(request, 'chef_info.html', {
                'chef_info' : chef_info, 'comments': comments, 'form': form 
            })
    else:
        form = CommentForm()
    return render(request, 'chef_info.html', {
        'chef_info' : chef_info, 'comments': comments, 'form': form
    })


@login_required(login_url='/accounts/login/')
def my_profile(request):
    """
    Renders the user's profile page if authenticated,
    Otherwise redirects to login page
    """

    return render(request, 'my_profile.html', {
        'my_profile' : my_profile
    })


@login_required(login_url='/accounts/login/')
def edit_profile(request):
    """
    Allows users to edit their profile information.
    If the request method is POST:
        - Validates and saves the updated user profile.
        - Displays a success message if the profile is updated successfully.
        - Redirects to the 'my_profile' page.
        - If the profile update fails, displays an error message.
    If the request method is not POST:
        - Initializes a form with the existing user profile data.
        - Renders the 'edit_profile.html' template with the form.
    """

    profile, created = Profile.objects.get_or_create(user=request.user)
    if request.method == 'POST':
        form = UserProfileForm(request.POST, request.FILES, instance=profile)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your profile has been updated successfully.')
            return redirect('chefs:my_profile')
        else:
            messages.error(request, 'Your profile update encountered an error.')
            return render(request, 'edit_profile.html', {'form': form})
    else:
        form = UserProfileForm(instance=profile)
    return render(request, 'edit_profile.html', {'form': form})


@login_required(login_url='/accounts/login/')
def delete_profile(request):
    """
    Deletes the user's profile upon receiving a POST request.
    If the request method is POST:
        - Deletes the user account associated with the request.
        - Displays a success message indicating successful deletion.
        - Redirects to the 'home' page.
    If the request method is not POST:
        - Renders the 'delete_profile.html' template.
    """

    if request.method == 'POST':
        user = request.user
        user.delete()
        messages.success(request, 'Your profile has been deleted successfully.')
        return redirect('home') 
    return render(request, 'delete_profile.html')