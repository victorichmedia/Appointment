from django.db import models
from django.contrib.auth.models import BaseUserManager, AbstractBaseUser
from django.utils.translation import ugettext_lazy as _
from django.urls import reverse

# Create your models here.

class UserManager(BaseUserManager):
    def create_user(self, username, password, **kwargs):
        if not username:
            raise ValueError('Users must have an username')

        user = self.model(
            username=username,
            email=email,
            **kwargs
        )
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, username, email, password, **kwargs):
        user = self.create_user(
            username,
            password=password,
        )
        user.is_superuser = True
        user.is_staff = True
        user.save(using=self._db)
        return user

class User(AbstractBaseUser):
    username = models.CharField(max_length=20, unique=True)
    email = models.EmailField('email address', blank=True, unique=True)
    first_name = models.CharField(max_length=50, blank=True)
    last_name = models.CharField(max_length=50, blank=True)
    is_staff = models.BooleanField('staff status', default=False)
    is_active = models.BooleanField(default=True)

    objects = UserManager()

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['first_name', 'last_name']

    def get_absolute_url(self):
        """Returns the url to access a particular doctor instance."""
        return reverse('user-detail', args=[str(self.id)])

    def __str__(self):
      return self.username


class Doctor(models.Model):
    """Model representing an author."""
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    date_of_birth = models.DateField(null=True, blank=True)
    is_staff = models.BooleanField('staff status', default=True)
    specification = models.ManyToManyField('Specification')
   
  
    def get_absolute_url(self):
        """Returns the url to access a particular doctor instance."""
        return reverse('doctor-detail', args=[str(self.id)])

    def __str__(self):
        """String for representing the Model object."""
        return f'{self.first_name}, {self.last_name}'

class Specification(models.Model):
    """Model representing doctor specification."""
    name = models.CharField(max_length=200, help_text='What is your specification (e.g. Medical Doctor)')
    
    def __str__(self):
        """String for representing the Model object."""
        return self.name

