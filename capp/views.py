from django.shortcuts import render,redirect
from django.http import Http404, HttpResponse
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
# from .models import Neighborhood,Post,Business,Profile,Follow
from .forms import ProfileForm, QuestionForm, CommentForm

from wsgiref.util import FileWrapper
import mimetypes
from django.conf import settings
import os

@login_required(login_url='/accounts/login')
def index(request):
    title = 'BADILI'
    questions = Question.get_questions
    return render(request, 'index.html', {"title": title, "questions":questions})

@login_required(login_url='/accounts/login/')
def post_question(request):
    current_user = request.user
    if request.method == 'POST':
        form = QuestionForm(request.POST, request.FILES)
        if form.is_valid():
            opinion = form.save(commit = False)
            opinion.user = current_user
            opinion.save()
        return redirect(index)
    else:
        form = QuestionForm()
    return render(request, 'question.html', {"form": form, "current_user":current_user})

@login_required(login_url='/accounts/login/')
def all_questions(request):
    title = 'BADILI'
    questions = Question.get_questions
    return render(request, 'view-question.html', {"title": title, "questions":questions})
