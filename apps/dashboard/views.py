from django.shortcuts import render
from django.contrib.auth.decorators import login_required
# from django.contrib.auth.models import Group
# from .decorators import allowed_users, admin_only

from apps.auth.decorators import allowed_users
# Create your views here.
@login_required(login_url='login')
@allowed_users(allowed_roles=['admin'])
def index(request):
    return render(request, 'Dashboard/index.html')