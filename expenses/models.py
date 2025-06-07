from django.db import models
from django.contrib.auth.models import AbstractUser


'''extending django's inbuilt User model'''
class User(AbstractUser):
    email = models.EmailField(unique=True)
    USERNAME_FIELD = 'email'    #making email as default username for the login
    REQUIRED_FIELDS = ['username']

class Expense(models.Model):
    CATEGORIES = [
        ('Food', 'FOOD'),
        ('Travel', 'TRAVEL'),
        ('Utilities', 'UTILITIES'),
        ('Other', 'OTHER'),
    ]

    user = models.ForeignKey(User, on_delete=models.CASCADE) #automatically deletes when the user is deleted
    amount = models.FloatField()
    category = models.CharField(max_length=20, choices=CATEGORIES)
    date = models.DateField()
    note = models.TextField(blank = True)