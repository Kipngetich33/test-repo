from django.contrib import admin
from .models import Profile, Question, Comment, Session

# Register your models here.

admin.site.register(Profile)
admin.site.register(Comment)
admin.site.register(Question)
admin.site.register(Session)
