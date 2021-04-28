from django.db import models
from django.contrib.auth.models import AbstractBaseUser
# Create your models here.
class Booking(AbstractBaseUser):

    time = models.DateTimeField(auto_now=False, auto_now_add=False)
    user_id = models.CharField(max_length = 200)
    advisor_id = models.CharField(max_length = 200)


    username = None
    USERNAME_FIELD = 'user_id'
    REQUIRED_FIELDS = []
