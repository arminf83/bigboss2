from django.db import models
from django.contrib.auth.models import AbstractUser , UserManager
from .usermanager import CustomUsermanager
from django.core.validators import MinValueValidator, MaxValueValidator


class User(AbstractUser):
    GENDER_CHOICES = [
        ('male', 'male'),
        ('female', 'female'),
        ('other', 'perfer not to say'),
    ]
    username=None
    first_name=models.CharField(max_length=50)
    last_name=models.CharField(max_length=50)
    born_date=models.DateField(null=True,blank=True)
    email=models.EmailField(max_length=254, unique=True)
    password=models.CharField(max_length=100)
    gender=models.CharField(max_length=50,choices=GENDER_CHOICES,default='other')
    personal_code=models.CharField(max_length=10 , null=True,blank=True)
    avatar=models.ImageField(upload_to=None,null=True,blank=True)

    def __str__(self):
            return self.email  

    objects=CustomUsermanager()
    REQUIRED_FIELDS=[]
    USERNAME_FIELD = 'email'
    backend='user.backend.EmailBackend'


# class Comment(models.Model):
#     STARCHOICE = [
#         (0, '0'),
#         (1, '1'),
#         (2, '2'),
#         (3, '3'),
#         (4, '4'),
#         (5, '5'),
#     ]
    
#     text = models.CharField(max_length=50)
#     star = models.SmallIntegerField(choices=STARCHOICE, default=0, validators=[
#             MinValueValidator(0),
#             MaxValueValidator(5)
#     ])
#     commenter = models.ForeignKey(User, on_delete=models.CASCADE)
#     sent_date = models.DateTimeField(auto_now_add=True)

#     def __str__(self):
#         return self.text[:50]


class Bank_user(models.Model):
    User=models.ForeignKey(User, on_delete=models.CASCADE)
    account_name=models.CharField(max_length=50)
    bank_name=models.CharField(max_length=50)
    account_number=models.IntegerField()
    kart_number=models.IntegerField()
    shaba_number=models.IntegerField()

class Adress_user(models.Model):

    User=models.ForeignKey(User,on_delete=models.CASCADE)
    postal_code=models.PositiveIntegerField()
    city=models.CharField(max_length=50)
    address=models.CharField(max_length=50)
    province=models.CharField(max_length=50)

