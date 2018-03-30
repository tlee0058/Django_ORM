# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from .models import Dojo, Ninja
from django.shortcuts import render, HttpResponse, redirect

# Create your views here.
def index(request):
    return HttpResponse('Hello')