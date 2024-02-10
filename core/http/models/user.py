from django.contrib.auth.models import AbstractUser, BaseUserManager
from django.db import models

from common.env import env


class UserManager(BaseUserManager):

    def create_user(self, phone, password=None, **extra_fields):
        if not phone:
            raise ValueError('The phone number must be set')

        user = self.model(phone=phone, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, phone, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')

        return self.create_user(phone, password, **extra_fields)


class User(AbstractUser):
    phone = models.CharField(max_length=255, unique=True)
    USERNAME_FIELD = u"phone"

    objects = UserManager()

    def __str__(self):
        return self.phone


class PendingUser(models.Model):
    phone = models.CharField(max_length=20)
    code = models.CharField(max_length=8, blank=True, null=True)
    password = models.CharField(max_length=255, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{str(self.phone)}: {self.code}"

    def is_valid(self) -> bool:
        """10 mins OTP validation"""
        lifespan_in_seconds = float(env("OTP_EXPIRE_TIME") * 60)
        now = datetime.now(timezone.utc)
        time_diff = now - self.created_at
        time_diff = time_diff.total_seconds()
        if time_diff >= lifespan_in_seconds:
            return False
        return True
