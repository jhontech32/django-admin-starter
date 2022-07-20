import requests

from django.shortcuts import render

from django.contrib.auth.decorators import login_required

from .forms import CustomerForm

# Create your views here.
@login_required(login_url='login')
def dashboard(request):
    return render(request, 'Dashboard/index.html')

@login_required(login_url='login')
def profile(request):
    # customer = request.user.customer_user
    # print('customerx', customer)
    # form = CustomerForm(instance=customer)
    #
    # if request.method == 'POST':
    #     form = CustomerForm(request.POST, request.FILES, instance=customer)
    #     if form.is_valid():
    #         form.save()

    context = {
        'page': 'Profile'
        # 'form': form
    }
    return render(request, 'Account/profile.html', context)

def members(request):
   customer = request.user.customer
   form = CustomerForm(instance=customer)

   if request.method == 'POST':
       form = CustomerForm(request.POST, request.FILES, instance=customer)
       if form.is_valid():
           form.save()

   context = {'form': form}
   return render(request, 'Members/index.html', context)

def posted(request):
    # pull data from third party rest api
    response = requests.get('https://jsonplaceholder.typicode.com/posts')

    # convert reponse data into json
    posts = response.json()

    context = {
        'page': 'Posted',
        'posts': posts
    }
    return render(request, 'Posted/index.html', context)
