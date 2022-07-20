from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='notification'),
    path('send/', views.send, name='send')
]
