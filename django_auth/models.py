from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager


class CustomUserManager(BaseUserManager):
    def create_user(self, email, password=None, is_active=True,
                    is_practitioner=False, is_admin=False, is_superuser=False, is_staff=False):
        if not email:
            raise ValueError("You must provide an email to register")
        if not password:
            raise ValueError("You must provide a password")

        email=self.normalize_email(email)
        user_obj = self.model(email=email)
        user_obj.set_password(password)
        user_obj.practitioner = is_practitioner
        user_obj.admin = is_admin
        user_obj.superuser = is_superuser
        user_obj.active = is_active
        user_obj.staff = is_staff
        user_obj.save(using=self._db)
        return user_obj

    def create_practitioner(self, email, password=None):
        user = self.create_user(
            email,
            password,
            is_practitioner=True
        )
        return user

    def create_superuser(self, email, password=None):
        user = self.create_user(
            email,
            password=password,
            is_admin=True,
            is_staff=True,
            is_superuser=True
        )
        return user


class CustomUser(AbstractBaseUser):
    email = models.EmailField(max_length=255, unique=True)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    active = models.BooleanField(default=True)  # Able to login
    practitioner = models.BooleanField(default=False)  # has access to a clinc
    admin = models.BooleanField(default=False)  # superuser
    staff = models.BooleanField(default=False)  # staff
    superuser = models.BooleanField(default=False)  # another superuser?
    timestamp = models.DateTimeField(auto_now_add=True)
    

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = CustomUserManager()

    def __str__(self):
        return self.email

    def get_full_name(self):
        return self.first_name + " " + self.last_name

    def get_short_name(self):
        return self.first_name

    def has_perm(self, perm, obj=None):
        return True

    def has_module_perms(self, app_label):
        return True

    @property
    def is_staff(self):
        return self.staff

    @property
    def is_practitioner(self):
        return self.practitioner

    @property
    def is_admin(self):
        return self.admin

    @property
    def is_active(self):
        return self.active

    @property
    def is_superuser(self):
        return self.superuser

