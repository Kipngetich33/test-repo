from django.shortcuts import render,redirect
from django.http import Http404, HttpResponse
# from django.core.exceptions import ObjectDoesNotExist
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
# from .models import Neighborhood,Post,Business,Profile,Follow

from wsgiref.util import FileWrapper
import mimetypes
from django.conf import settings
import os

@login_required(login_url='/accounts/login')
def index(request):

    title = 'Timeline'


    return render(request, 'index.html', {"title": title})
