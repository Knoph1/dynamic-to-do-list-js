from django.contrib.auth.models import AbstractUser 
from django.db import models
from .managers import CustomUserManager

# Create your models here.
class CustomUser(AbstractUser):
    date_of_birth = models.DateField(null=True, blank=True)
    profile_photo = models.ImageField(upload_to='profile_photos/', null=True, blank=True)

    objects = CustomUserManager()

    def __str__(self):
        return self.username

class ExampleModel(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()

    class Meta:
        permissions = [
            ("can_view", "Can view items"),
            ("can_create", "Can create items"),
            ("can_edit", "Can edit items"),
            ("can_delete", "Can delete items"),
        ]
        def __str__(self):
            return self.name

class CustomUserManager(CustomUserManager): 
    def create_user(self, email, date_of_birth, password=None, **extra_fields): 
        if not email: 
            raise ValueError('The Email field must be set') 
        email = self.normalize_email(email)
        user = self.model(email=email, date_of_birth=date_of_birth, **extra_fields) 
        user.set_password(password) 
        user.save(using=self._db) 
        return user 
        def create_superuser(self, email, date_of_birth, password=None, **extra_fields): 
            extra_fields.setdefault('is_staff', True) 
            extra_fields.setdefault('is_superuser', True) 
            
            if extra_fields.get('is_staff') is not True: 
                raise ValueError('Superuser must have is_staff=True.') 
            
            if extra_fields.get('is_superuser') is not True: 
                raise ValueError('Superuser must have is_superuser=True.') 
                
            return self.create_user(email, date_of_birth, password,)

class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=100)
    publication_year = models.IntegerField()

    def __str__(self):
        return self.title
