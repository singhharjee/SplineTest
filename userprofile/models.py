from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager


class UserManager(BaseUserManager):
    def create_user(self, email, password=None):
        if email is None:
            raise ValueError('User must have email')

        user = self.model(email=email)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, password, email):
        user = self.create_user(
            email=self.normalize_email(email), password=password)
        user.is_admin = True
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)
        return user


class User(AbstractBaseUser):
    email = models.EmailField(
        verbose_name='email', max_length=60, default=None, null=True, unique=True)
    password = models.CharField(max_length=10)
    name = models.CharField(max_length=30, blank=True)
    age = models.CharField(max_length=30, blank=True)
    gender = models.CharField(max_length=30, blank=True)
    phone = models.IntegerField(blank=True, null=True)
    address = models.CharField(max_length=30, blank=True)
    img = models.ImageField(blank=True)

    date_joined = models.DateTimeField(
        verbose_name='date joined', auto_now_add=True)
    last_login = models.DateTimeField(verbose_name='last login', auto_now=True)
    is_admin = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELD = ['email']
    objects = UserManager()

    def __str__(self):
        return self.email

    # For checking permissions. to keep it simple all admin have ALL permissons
    def has_perm(self, perm, obj=None):
        return self.is_admin

    # Does this user have permission to view this app? (ALWAYS YES FOR SIMPLICITY)
    def has_module_perms(self, app_label):
        return True
