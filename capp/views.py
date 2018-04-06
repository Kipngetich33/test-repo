from django.shortcuts import render,redirect
from django.http import Http404, HttpResponse
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from .models import Profile, Question, Comment, Session
from .forms import ProfileForm, QuestionForm, CommentForm

from wsgiref.util import FileWrapper
import mimetypes
from django.conf import settings
import os

@login_required(login_url='/accounts/login')
def index(request):
    title = 'BADILI'

    return render(request, 'index.html', { "title": title})

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
def post_comment(request, q_id):
    current_question = Question.objects.get(id=q_id)
    current_user = request.user
    if request.method == 'POST':
        form = CommentForm(request.POST, request.FILES)
        if form.is_valid():
            comment = form.save(commit = False)
            comment.user = current_user
            comment.post = current_question
            comment.save()
        return redirect(single_image,current_question.id)
    else:
        form = CommentForm()
    return render(request, 'comment.html', {"form": form})


@login_required(login_url='/accounts/login/')
def all_questions(request):
    title = 'BADILI'
    questions = Question.get_questions
    return render(request, 'all-questions.html', {"title": title, "questions":questions})


@login_required(login_url='/accounts/login/')
def single_question(request,question_id):
    title = 'BADILI'
    question = Question.objects.get(id=question_id)
    return render(request, 'single-question.html', {"title": title, "question":question})


@login_required(login_url='/accounts/login/')
def unbooked_session(request):
    title = 'BADILI'
    sessions = Session.get_sessions
    return render(request, 'booking.html', { "title": title, "sessions":sessions})
