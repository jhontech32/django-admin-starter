from django.forms import ModelForm

from .models import *

class CustomerForm(ModelForm):
	class Meta:
		model = Customer
		fields = ('name', 'phone', 'email', 'profile_pic')
