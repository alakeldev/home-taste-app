from django.urls import path
from . import views

app_name = 'chefs'
urlpatterns = [
    path('', views.chefs_list, name='chefs_list'),
    path('<slug:slug>/', views.chef_info, name='chef_info'),
    path('myprofile/', views.my_profile, name='my_profile'),
]