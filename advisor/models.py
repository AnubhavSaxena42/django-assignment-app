from django.db import models 
from django.contrib.auth.models import AbstractBaseUser
class Advisor(AbstractBaseUser):
    name = models.CharField(max_length=200)
    photo_url = models.CharField(max_length = 100)