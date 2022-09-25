import uuid

from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from django.utils.translation import gettext_lazy as _

class CustomUserManager(BaseUserManager):
    '''
    Class to create a user
    '''
    def create_user(self, email, full_name, password=None):
        if not email:
            raise ValueError("E-mail is required.")
        if not full_name:
            raise ValueError("Full Name is required.")

        user = self.model(
            email = self.normalize_email(email),
            full_name =  full_name,
        )

        user.set_password(password)

        user.save(using=self._db)
        return user

    def create_superuser(self, email, full_name, password):

        user = self.create_user(
            email = self.normalize_email(email),
            password = password,
            full_name = full_name,
        )

        user.is_admin = True
        user.is_staff = True
        user.is_superuser = True

        user.save(using=self._db)
        return user

class CustomUser(AbstractBaseUser):
    '''
    Model to create a custom user on django
    '''
    id_user = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    full_name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100, unique=True)
    date_joined = models.DateTimeField(auto_now_add=True)
    last_login = models.DateTimeField(auto_now=True)
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['full_name', ]

    objects = CustomUserManager()

    def __str__(self):
        return self.email
    
    def has_perm(self, perm, obj=None):
        return self.is_admin

    def has_module_perms(self, app_label):
        return True