# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import re, bcrypt, datetime
from django.db import models
EMAIL_REGEX=re.compile(r'^[a-zA-Z0-9\.\+_-]+@[a-zA-Z0-9\._-]+\.[a-zA-Z]*$')

# Create your models here.
class UserdbManager(models.Manager):
    def validator(self, postData):
        print "postdata + {}".format(postData)
        errors = []
        check_email = Userdb.objects.filter(email=postData['email'])
        if len(check_email) >1:
            errors.append("Email is already existed, please log in")

        else:   
        
            if not EMAIL_REGEX.match(postData['email']):
                errors.append("Email not valid")            
            if len(postData['first_name']) < 1:
                errors.append("First name cannot be blank")
            if len(postData['last_name']) < 1:
                errors.append("Last name cannot be blank")

            # if len(postData['password']) < 8:
            #     errors.append("Email must be at least 8 characters")
            # if postData['password'] != postData['confirm_pw']:
            #     errors.append("Your passwords do not match")
        return errors    
        
    def creator(self, cleanData):
        #hashed_pw = bcrypt.hashpw(cleanData['password'].encode(), bcrypt.gensalt())
        return self.create(
            first_name = cleanData['first_name'],
            last_name = cleanData['last_name'],
            email = cleanData['email'],
            #password = hashed_pw,
        )

    def update(self, update_data):
        return self.create(
            first_name = update_data['first_name'],
            last_name = update_data['last_name'],
            email = update_data['email'],
        )


        

class Userdb(models.Model):
    first_name=models.CharField(max_length = 255)
    last_name = models.CharField(max_length = 255)
    email = models.CharField(max_length = 255)
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = UserdbManager()



