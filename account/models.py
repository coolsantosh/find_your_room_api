from django.db import models
from django.contrib.auth.models import BaseUserManager, AbstractBaseUser
import uuid


DISTRICT_CHOICES=[
    ("Kathmandu","Kathmandu"),
    ("Pokhara","Pokhara")
]
CITY_CHOICES=[
    ("Kathmandu","Kathmandu"),
    ("Pokhara","Pokhara")
]




class UserManager(BaseUserManager):
    def create_user(self, email,name,address,mobile,city,district,password=None,password2=None):
       
        if not email:
            raise ValueError("Users must have an email address")

        user = self.model(
            email=self.normalize_email(email),
            name=name,
            address=address,
            mobile=mobile,
            city=city,
            district=district,

        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, name,address,mobile,city,district, password=None):
       
        user = self.create_user(
            email,
            password=password,
            name=name,
            address=address,
            mobile=mobile,
            city=city,
            district=district,
            
        )
        user.is_admin = True
        user.save(using=self._db)
        return user

class User(AbstractBaseUser):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    email = models.EmailField(
        verbose_name="email_address",
        max_length=255,
        unique=True,
    )
    name=models.CharField(max_length=200)
    address=models.TextField()
    mobile=models.IntegerField()
    city=models.CharField(max_length=100,choices=CITY_CHOICES)
    district=models.CharField(max_length=100,choices=DISTRICT_CHOICES)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)

    objects = UserManager()

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["name","address","mobile","city","district"]

    def __str__(self):
        return self.email

    def has_perm(self, perm, obj=None):
        "Does the user have a specific permission?"
        # Simplest possible answer: Yes, always
        return True

    def has_module_perms(self, app_label):
        "Does the user have permissions to view the app `app_label`?"
        # Simplest possible answer: Yes, always
        return True

    @property
    def is_staff(self):
        "Is the user a member of staff?"
        # Simplest possible answer: All admins are staff
        return self.is_admin
