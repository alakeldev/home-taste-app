from django.urls import path
from . import views

app_name = 'accounts'
urlpatterns = [
    path('chefs/', views.chefs, name='chefs_accounts'),
    path('chefs/<slug:slug>/', views.chef_info, name='chef_info'),
    path('chefs/login/', views.user_login, name='login'),
]