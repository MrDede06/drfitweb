from __future__ import unicode_literals
from django.utils.encoding import force_text
from django.db import models
import datetime
from django.utils import timezone



class Users(models.Model):
    facebookid = models.CharField(max_length=1000,blank=True , null=True)
    gmailid = models.CharField(max_length=1000,blank=True , null=True)
    phonetype = models.CharField(max_length=1000,blank=True , null=True)
    name = models.CharField(max_length=1000,blank=True , null=True)
    surname = models.CharField(max_length=1000,blank=True , null=True)
    notification = models.CharField(max_length=1000,blank=True , null=True)
    email = models.EmailField(max_length=1000,blank=True , null=True)
    password = models.CharField(max_length=1000,blank=True , null=True)
    gender = models.CharField(max_length=1000,blank=True , null=True)
    kilo = models.IntegerField(blank=True , null=True)
    height = models.IntegerField(blank=True , null=True)
    btype = models.IntegerField(blank=True , null=True)
    usertype = models.IntegerField(blank=True , null=True)
    point = models.IntegerField(blank=True , null=True)
    goal =  models.CharField(max_length=1000,blank=True , null=True)
    place = models.CharField(max_length=1000,blank=True , null=True)
    traindayinweek = models.CharField(max_length=1000,blank=True , null=True)
    profilephoto = models.FileField(blank=True, null=True)
    birthday = models.DateTimeField(null=True)
    def __unicode__(self):
        return '%s %s' % (self.id, self.name)

class Category(models.Model):
    name_en = models.TextField(max_length=1000,blank=True , null=True)
    name_tr = models.TextField(max_length=1000,blank=True , null=True)
    explain_en = models.TextField(max_length=1000,blank=True , null=True)
    explain_tr = models.TextField(max_length=1000,blank=True , null=True)
    image = models.TextField(max_length=1000,blank=True , null=True)
    def __unicode__(self):
        return u'Category name : %s ' % (self.id)


class SubCategory(models.Model):
    Ctgry = models.ForeignKey(Category,blank=True, on_delete=models.CASCADE  , null=True)
    image = models.TextField(max_length=1000,blank=True , null=True)
    totaltime = models.TextField(max_length=1000,blank=True , null=True)
    place = models.TextField(max_length=1000,blank=True , null=True)
    isitpremium = models.BooleanField('premium')
    name_en = models.TextField(max_length=1000,blank=True , null=True)
    name_tr = models.TextField(max_length=1000,blank=True , null=True)
    explain_en = models.TextField(max_length=1000,blank=True , null=True)
    explain_tr = models.TextField(max_length=1000,blank=True , null=True)
    def __unicode__(self):
        return u'%s' % (self.id)


class Program(models.Model):
    name_en = models.TextField(max_length=1000,blank=True , null=True)
    name_tr = models.TextField(max_length=1000,blank=True , null=True)
    explain_en = models.TextField(max_length=1000,blank=True , null=True)
    explain_tr = models.TextField(max_length=1000,blank=True , null=True)
    video = models.FileField(blank=True, null=True)
    def __unicode__(self):
        return u"name : %s "% (self.name_en)

class Form_test(models.Model):
    name_test = models.TextField(max_length=1000,blank=True , null=True)
    explain_test = models.TextField(max_length=1000,blank=True , null=True)
    def __unicode__(self):
        return u'Category name : %s ' % (self.id)
