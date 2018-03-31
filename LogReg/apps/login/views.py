# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from .models import Userdb
from django.shortcuts import render, HttpResponse, redirect
from django.contrib import messages
# Create your views here.

def index(request):
   
    return render(request, 'login/index.html')

def register(request):
    print request.POST
    validation = Userdb.objects.validator(request.POST)
    if len(validation) > 0:
        for e in validation:
            messages.error(request, e)
        return redirect ('/')
    else:
        new_record = Userdb.objects.creator(request.POST)
        request.session['id'] = new_record.id ##

        return redirect ('/success')

def success(request):
    context = {
        'user' : Userdb.objects.get(id=request.session['id'])
    }


    return render(request, 'login/success.html', context)

def login(request):
    val = Userdb.objects.check_login(request.POST)
    if len(val) > 0:
        for e in val:
            messages.error(request, e)
            
    else:
        print val
        return redirect ('/success')

    return redirect ('/')
