from django.shortcuts import render
from .forms import CustomerForm

# Create your views here.
def profile(request):
    customer = request.user.customer_user
    print('customerx', customer)
    form = CustomerForm(instance=customer)

    if request.method == 'POST':
        form = CustomerForm(request.POST, request.FILES, instance=customer)
        if form.is_valid():
            form.save()

    context = {
        'page': 'Profile',
        'form': form
    }
    return render(request, 'Account/profile.html', context)
