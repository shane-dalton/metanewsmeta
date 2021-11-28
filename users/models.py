from django.db import models
from django.utils.translation import gettext_lazy as _
# Create your models here.


from django.contrib.auth.models import AbstractBaseUser


class User(AbstractBaseUser):

    email = models.EmailField(_('Personal Email address'), unique=True)
    USERNAME_FIELD = 'email'

