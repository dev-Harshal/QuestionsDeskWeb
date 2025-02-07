from django.db import models
from django.contrib.auth.models import BaseUserManager, AbstractBaseUser 

# Create your models here.

class UserManager(BaseUserManager):

    def create_user(self, email, password=None, **extra_fields):
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using = self._db)
        return user
    
    def create_superuser(self, email, password=None, **extra_fields):
        extra_fields.setdefault('role', 'Admin')
        return self.create_user(email, password, **extra_fields)
        
class User(AbstractBaseUser):
    id = models.AutoField(primary_key=True)
    first_name = models.CharField(max_length=100, null=False, blank=False)
    last_name = models.CharField(max_length=100, null=False, blank=False)
    email = models.EmailField(unique=True, null=False, blank=False)
    username = models.CharField(max_length=100, unique=True, null=False, blank=False)
    password = models.CharField(max_length=100, null=False, blank=False)
    role = models.CharField(max_length=100, null=False, blank=False)
    institute = models.CharField(max_length=100, null=False, blank=False, default='SSVPS')
    joined_date = models.DateField(auto_now_add=True)
    
    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['first_name', 'last_name', 'email']
    objects = UserManager()

    def __str__(self):
        return self.email

    class Meta:
        db_table = 'Users Table'

class Subject(models.Model):
    name = models.CharField(max_length=100, null=True, blank=False)

    def __str__(self):
        return self.name
        
class StaffProfile(models.Model):
    user = models.OneToOneField(User, related_name='profile' ,on_delete=models.CASCADE)
    phone_number = models.CharField(max_length=10, null=False, blank=False)
    department = models.CharField(max_length=100, null=False, blank=False)
    subjects = models.ManyToManyField(Subject, null=True, blank=True, related_name='subject')

