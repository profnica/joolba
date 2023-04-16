from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager


class UserManager(BaseUserManager):
	
	def create_user(self, name, email, password=None, **kwargs):

		if not email:
			raise ValueError('Kindly enter your email address')

		
		user = self.model(name=name, email=email, **kwargs)
		user.set_password(password)
		user.save(using=self._db)
		return user

	def create_superuser(self, name, email, password):
		"""
		called create_user to create the user and added new property to the user as a superuser
		"""
		user = self.create_user(name, email, password)
		user.is_superuser = True
		user.is_staff = True
		user.save(using=self._db)
		return user 



class User(AbstractBaseUser):

	name = models.CharField(max_length=200) #can be users full name too, something to identify them
	email = models.EmailField(max_length=255, unique=True)
	is_active = models.BooleanField(default=True)
	is_superuser = models.BooleanField(default=False)
	is_staff = models.BooleanField(default=False)
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)

	USERNAME_FIELD = 'email'
	REQUIRED_FIELDS = ['name']


	objects = UserManager()

	def __str__(self):
		return str(self.email)

	def has_perm(self, perm, obj=None):
		return True
	
	def has_module_perms(self, app_label):
		return True