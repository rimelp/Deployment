# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
class CourseManager(models.Manager):
    def validate(self, postData):
        errors = {}
        if len(postData['name']) < 5:
            errors['name'] = "Course name must be at least 5 characters long"
        if len(postData['desc']) <15:
            errors['desc'] = "Course description must be at least 15 characters long"
        return errors

class Course(models.Model):
    name = models.CharField(max_length=255)
    desc = models.TextField(max_length=1000)
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)
    objects = CourseManager()

    def __str__(self): 
        return self.name + ' ' + self.desc