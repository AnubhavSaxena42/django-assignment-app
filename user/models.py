from django.db import models
from django.contrib.auth.models import AbstractBaseUser,BaseUserManager

#Custom user model for using email field for authentication purposes
class User(AbstractBaseUser):
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length = 250)

    username = None
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    