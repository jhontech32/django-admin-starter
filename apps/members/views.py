from django.shortcuts import render

from .forms import CustomerForm

# Create your views here.
def index(request):
   customer = request.user.customer
   form = CustomerForm(instance=customer)

   if request.method == 'POST':
       form = CustomerForm(request.POST, request.FILES, instance=customer)
       if form.is_valid():
           form.save()

   context = {'form': form}
   return render(request, 'Members/index.html', context)