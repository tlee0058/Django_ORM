# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, HttpResponse, redirect
from django.contrib import messages
# Create your views here.
from .models import Userdb, UserdbManager

def index(request):
    context = {
        'users' : Userdb.objects.all()
    }
    return render(request, 'users/index.html', context)

def new(request):
    return render(request, 'users/new.html')

def create(request):
    validator = Userdb.objects.validator(request.POST)
    if len(validator) > 0:
        for e in validator:
            messages.error(request, e)
            return redirect ('/users/new')
    else:
        Userdb.objects.creator(request.POST)
        print request.POST
        return redirect ('/users')

def show(request, id):
    
    if request.method == "POST":
        edit_data = Userdb.objects.get(id=id).update(request.POST)
        edit_data.save()
    

    context = {
        'user' : Userdb.objects.get(id = id),
    }
    
    return render(request, 'users/show.html', context)

def edit(request, id):
    context = {
        'user' : Userdb.objects.get(id = id),
    }

    return render(request, 'users/edit.html', context)

def destroy(request, id):
    
    Userdb.objects.get(id=id).delete(request.POST)
    

    return redirect ('/users')

    
    
        

        