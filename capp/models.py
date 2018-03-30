from django.db import models
from django.contrib.auth.models import User
import datetime as dt

# Create your models here.
class Profile(models.Model):
    user_type = models.CharField(max_length=10,default='patient')
    first_name = models.CharField(max_length =30)
    last_name = models.CharField(max_length =30)
    email = models.EmailField()
    phone_number = models.CharField(max_length = 10,blank =True)
    addiction = models.CharField(max_length = 200)
    duration = models.DateTimeField(auto_now_add=True, null=True)
    age = models.CharField(max_length = 10,blank =True)


class Question(models.Model):
    topic = models.CharField(max_length=150)
    date_asked = models.DateTimeField(auto_now_add=True, null=True)
    user = models.ForeignKey(User)

class Comment(models.Model):
    opinion = models.CharField(max_length=200)
    question = models.ForeignKey(Question)
    user = models.ForeignKey(User)

class Session(models.Model):
    Availability = models.BooleanField(default=True)
    Duration = models.DateTimeField(auto_now_add=True, null=True)
    sloted_date = models.DateTimeField(null=True)
    Doctor = models.CharField(max_length=30)
