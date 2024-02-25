from django.urls import path
from . import views

app_name = 'chefs'
urlpatterns = [
    path('', views.chefs_list, name='chefs_list'),
]