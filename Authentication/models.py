from django.db import models
from django.contrib.auth.models import Group, Permission
from django.contrib.auth.models import (
    AbstractBaseUser,
    BaseUserManager,
    PermissionsMixin,
)


class Role(models.Model):
    ROLE_CHOICES = [
        ("admin", "Admin"),
        ("member", "Member"),
        ("author", "Author"),
    ]
    name = models.CharField(max_length=20, choices=ROLE_CHOICES, unique=True)

    def __str__(self):
        return self.name


class CustomUserManager(BaseUserManager):
    def create_user(self, UserName, password=None, **extra_fields):
        user = self.model(UserName=UserName, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, UserName, password=None, **extra_fields):
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)
        return self.create_user(UserName, password, **extra_fields)


class UserBase(AbstractBaseUser, PermissionsMixin):
    UserName = models.CharField(max_length=85, unique=True)
    FName = models.CharField(max_length=75)
    LName = models.CharField(max_length=75)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    role = models.ForeignKey(Role, on_delete=models.SET_NULL, null=True, blank=True)

    USERNAME_FIELD = "UserName"
    REQUIRED_FIELDS = ["FName", "LName"]
    objects = CustomUserManager()

    groups = models.ManyToManyField(
        Group,
        related_name="custom_user_set",  # unique related_name to avoid clashes
        blank=True,
        help_text="The groups this user belongs to.",
        verbose_name="groups",
    )

    user_permissions = models.ManyToManyField(
        Permission,
        related_name="custom_user_set",  # unique related_name to avoid clashes
        blank=True,
        help_text="Specific permissions for this user.",
        verbose_name="user permissions",
    )

    def __str__(self):
        return self.UserName