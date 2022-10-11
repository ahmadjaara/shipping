import email
from email.policy import default
from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from django import forms

# Create your models here.
# class Service(forms.Form):
#   CHOICES = (
#       (1, 'fedex'),
#       (2, 'ups')      
#   )

class Post (models.Model):
   
    CHOICES = (
        ('FedEx service', (
            (1, 'fedexAIR'),
            (2, 'fedexGroud'),
        )),
        ('UPS service', (
            (3, 'UPSExpress'),
            (4, 'UPS2DAY'),
        ))
    )
    serviceship = models.CharField(max_length=10, choices=CHOICES, default="")
    
    # serviceShipID = models.CharField(max_length=250,default="not added")
    title = models.CharField(max_length=250)
    # seviceship=forms.ChoiceField(choices=Service)
    width =models.DecimalField(max_digits=10,decimal_places=1)
    height =models.DecimalField(max_digits=10,decimal_places=1)
    length =models.DecimalField(max_digits=10,decimal_places=1)
    weight =models.DecimalField(max_digits=10,decimal_places=1)
    # published = models.DateTimeField(default=timezone.now)
    custumer = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='user_shipping')

    # category = models.ForeignKey(Category, on_delete=models.PROTECT, default=1)
    # excerpt = models.TextField(null=True)
    # content = models.TextField()
    # slug = models.SlugField(max_length=250, unique_for_date='published')

    def __str__(self):
        return self.title
    
class Customer(models.Model):
    name=models.OneToOneField(User, on_delete=models.CASCADE)
    email=models.CharField(max_length=50)
    password=models.CharField(max_length=50)
    confirm_password=models.CharField(max_length=50)
    
    def __str__(self):
        return self.name
