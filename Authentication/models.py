from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin


class UserBase(AbstractBaseUser, PermissionsMixin):
    FName = models.CharField(max_length=75)
    LName = models.CharField(max_length=75)
    Nc = models.CharField(max_length=11, unique=True,)

    USERNAME_FIELD = 'Nc'
    REQUIRED_FIELDS = ['FName','LName']


class CustomUserManager(BaseUserManager):
    def create_user(self, Nc, password=None, **extra_fields):
        user = self.model(Nc=Nc, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, Nc, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        return self.create_user(Nc, password, **extra_fields)