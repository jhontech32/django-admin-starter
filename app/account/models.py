from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Customer(models.Model):
	# user = models.OneToOneField(User, null=True, blank=True, on_delete=models.CASCADE)
	user = models.OneToOneField(User, related_name='customer_user', null=True, blank=True, on_delete=models.CASCADE)
	name = models.CharField(max_length=200, null=True)
	phone = models.CharField(max_length=200, null=True)
	email = models.CharField(max_length=200, null=True)
	profile_pic = models.ImageField(default="user-role.png", null=True, blank=True)
	date_created = models.DateTimeField(auto_now_add=True, null=True)

	USERNAME_FIELD = 'profile_pic'
	# AUTH_USER_MODEL = 'user.customer_user'
	REQUIRED_FIELDS = ['username']

	# class Meta:
	# 	managed = False,
	# 	db_table = 'account_customer',
	# 	fields = '__all__'

	def __str__(self):
		return self.name


# class Tag(models.Model):
# 	name = models.CharField(max_length=200, null=True)
#
# 	def __str__(self):
# 		return self.name
#
# 	class Meta:
# 		managed = False
# 		db_table = 'apps_tag',
# 		fields = '__all__'