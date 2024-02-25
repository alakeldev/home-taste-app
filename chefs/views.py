from django.shortcuts import render
from django.contrib.auth.models import User
# Create your views here.


def chefs_list(request):
    chefs = User.objects.all()
    return render(request, 'chefs.html', {
        'chefs' : chefs,
    })