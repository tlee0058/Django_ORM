# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, HttpResponse, redirect
from models import Author, Book
# Create your views here.

def index(request):
    return HttpResponse("Hello")