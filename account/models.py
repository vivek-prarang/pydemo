from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    is_employee = models.BooleanField(default=False)
    is_client = models.BooleanField(default=False)
    ROLE=[
        ('Employee','employee'),
        ('Client','client'),
    ]
    role=models.CharField(max_length=10,default='employee',choices=ROLE)
