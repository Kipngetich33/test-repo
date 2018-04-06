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
    age = models.CharField(max_length = 10,blank =True)

    def __str__(self):
        return self.first_name

class Record(models.Model):
    date_checked = models.DateTimeField(auto_now_add=True, null=True)
    problem = models.CharField(max_length = 200)
    user = models.ForeignKey(User)


class Question(models.Model):
    topic = models.CharField(max_length=150)
    date_asked = models.DateTimeField(auto_now_add=True, null=True)
    user = models.ForeignKey(User)


    def __str__(self):
        return self.user.username

    @classmethod
    def get_questions(cls):
        questions = cls.objects.all()
        return questions


class Comment(models.Model):
    opinion = models.CharField(max_length=200)
    date_posted = models.DateTimeField(auto_now_add=True, null=True)
    question = models.ForeignKey(Question)
    user = models.ForeignKey(User)

    def __str__(self):
        return self.user.username

    @classmethod
    def get_comments(cls,question_id):
        comments = cls.objects.filter(question=question_id)
        return comments

class Doctor(models.Model):
    name = models.CharField(max_length=30)


class Session(models.Model):
    Availability = models.BooleanField(default=True)
    sloted_date = models.DateTimeField(auto_now_add=True, null=True)
    duration = models.TimeField( blank=True,null=True)
    # contact_date = models.DateField(_(u"Conversation Date"), blank=True)
    # contact_time = models.TimeField( blank=True)
    doctor = models.ForeignKey(Doctor)

    @classmethod
    def get_sessions(cls):
        sessions = cls.objects.all()
        return sessions
