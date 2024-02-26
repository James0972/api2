from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    account_balance = models.PositiveIntegerField(default=100)
    name=models.CharField(max_length=50)
    email=models.EmailField(max_length=50, unique=True)
    password=models.CharField(max_length=5000)
    username=None
    USERNAME_FIELD='email'
    REQUIRED_FIELDS=[]

