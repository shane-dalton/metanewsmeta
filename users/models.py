from django.db import models
from django.utils.translation import gettext_lazy as _
# Create your models here.


from django.contrib.auth.models import AbstractBaseUser


class User(AbstractBaseUser):

    first_name = models.CharField(max_length=25,null=True)
    last_name = models.CharField(max_length=25,null=True)
    phone = models.CharField(max_length=13, null=True)
    email = models.EmailField(_('Personal Email address'), unique=True)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    USERNAME_FIELD = 'email'

