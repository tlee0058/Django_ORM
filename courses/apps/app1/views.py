# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, HttpResponse, redirect

from django.contrib import messages

# Create your views here.
def index(request):
    context = {
        'courses' : Course.objects.all(),
        
    }
    return render(request, 'app1/index.html', context)

def add(request):
    val = Course.objects.validator(request.POST)

    if len(val):
        for e in val:
            messages.error(request, e)

    else:
        Course.objects.creator(request.POST)

    return redirect ('/')

def remove(request, id):
    Course.objects.get(id=id).delete()
   
    return redirect ('/')
        
