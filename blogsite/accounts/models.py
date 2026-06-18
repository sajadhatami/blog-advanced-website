import email

from django.db import models
from django.contrib.auth.models import (BaseUserManager,AbstractBaseUser,PermissionsMixin)

# Create your models here.


class User(AbstractBaseUser,PermissionsMixin):
    #customising user
    email = models.EmailField(unique=True,max_length=250)
    #USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []
    #is he staff user or not
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    # is verified 
    #is_verified = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    
    
    
    def __str__(self):
        return self.email