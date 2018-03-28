from django.db import models
from django.contrib.auth.models import User
import datetime as dt

# Create your models here.
class Question(models.Model):
    topic = models.CharField(max_length=150)
    date_asked = models.DateTimeField(auto_now_add=True, null=True)
    user = models.ForeignKey(User)

class Comment(models.Model):
    opinion = models.CharField(max_length=200)
    question = ForeignKey(Question)
    user = ForeignKey(User)

class Session(models.Model):
    Availability = models.BooleanField(default=True)
    Duration = models.DateTimeField(auto_now_add=True, null=True)
    sloted_date = models.DateTimeField(null=True)
    Doctor = models.CharField(max_length=30)
