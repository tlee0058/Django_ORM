# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.contrib import messages
# Create your models here
class CourseManager(models.Manager):
    
    def validator(self, postData):
        errors = []
       
            
        if len(postData['name']) < 6:
            errors.append("Name must be at least 5 characters")

        if len(postData['desc']) < 16:
            errors.append("Description must be at least 15 characters")

        return errors

    def creator(self, newData):
        
        return self.create(name=newData['name'], desc=newData['desc'])
        
class Desc(models.Model):
    content = models.TextField()
class Course(models.Model):
    name=models.CharField(max_length = 255)
    desc=models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = CourseManager()

