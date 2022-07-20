from django.urls import path
from . import views

urlpatterns = [
    path('dashboard', views.dashboard, name='dashboard'),
    path('members', views.members, name='members'),
    path('posted', views.posted, name='posted'),
    path('profile', views.profile, name='profile')
]
