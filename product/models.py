from django.db import models
from user.models import User
from django.core.validators import MinValueValidator, MaxValueValidator


class Category (models.Model):
    name=models.CharField(max_length=50)
    logo=models.ImageField(upload_to='productimage/')
    def __str__(self):
        return self.name[:50]



class Product (models.Model):
    STARCHOICE=[
        (0,0),
        (1,1),
        (2,2),
        (3,3),
        (4,4),
        (5,5),
    ]
    name=models.CharField(max_length=50)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, null=True)
    description=models.TextField(null=True, blank=True )
    price=models.CharField(max_length=50)
    offprice=models.PositiveSmallIntegerField(null=True, blank=True , default=0,
        validators=[
             MinValueValidator(0),
             MaxValueValidator(100)])
    stock=models.PositiveIntegerField()
    logo=models.ImageField(upload_to='productimage/')
    def __str__(self):
        return self.name[:50]

class Comment(models.Model):
    STARCHOICE=[
        (0,0),
        (1,1),
        (2,2),
        (3,3),
        (4,4),
        (5,5),
    ]
    
    # gender=models.CharField(max_length=50,choices=GENDER_CHOICES,default='other')


    text = models.CharField(max_length=50)
    # star = models.SmallIntegerField( validators=[
    #         MinValueValidator(0),
    #         MaxValueValidator(5)])
    star = models.CharField(choices=STARCHOICE ,max_length=1, default="0")
    product = models.ForeignKey(Product, on_delete=models.CASCADE, null=True)
    commenter = models.ForeignKey(User, on_delete=models.CASCADE)
    sent_date = models.DateTimeField(auto_now_add= True)
    like = models.PositiveSmallIntegerField()
    dislike = models.PositiveSmallIntegerField()
    def __str__(self):
        return self.text[:50]


class Color (models.Model):
    product=models.ForeignKey(Product, on_delete=models.CASCADE)
    name=models.CharField(max_length=50)



class Size (models.Model) :
    product=models.ForeignKey(Product, on_delete=models.CASCADE)
    name=models.CharField(max_length=50)





class Favorite (models.Model):
    user=models.ForeignKey(User, on_delete=models.CASCADE)
    product=models.ForeignKey(Product, on_delete=models.CASCADE)


