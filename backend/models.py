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
    name_tr = models.TextField(max_length=1000,blank=True , null=True)
    name_en = models.TextField(max_length=1000,blank=True , null=True)
    explain_tr = models.TextField(max_length=1000,blank=True , null=True)
    explain_en = models.TextField(max_length=1000,blank=True , null=True)    
    image = models.TextField(max_length=1000,blank=True , null=True)
    def __str__(self):
        return u'kategori Ismi : %s ' % (self.name_tr)


class SubCategory(models.Model):
    name_en = models.TextField(max_length=1000,blank=True , null=True)
    name_tr = models.TextField(max_length=1000,blank=True , null=True)
    explain_en = models.TextField(max_length=1000,blank=True , null=True)
    explain_tr = models.TextField(max_length=1000,blank=True , null=True)
    Ctgry = models.ForeignKey(Category,blank=True, on_delete=models.CASCADE  , null=True)
    image = models.TextField(max_length=1000,blank=True , null=True)
    totaltime = models.TextField(max_length=1000,blank=True , null=True)
    isitpremium = models.BooleanField('premium')
    def __str__(self):
        return u'Alt Kategori Ismi : %s ' % (self.name_tr)


class Programlist(models.Model):
    name_tr = models.TextField(max_length=1000,blank=True , null=True)
    psc = models.ForeignKey(SubCategory, on_delete=models.CASCADE, blank=False , null=False)
    setcount = models.IntegerField(blank=True , null=True, default=0)
    replycount = models.IntegerField(blank=True , null=True, default=0)
    resttime = models.IntegerField(blank=True , null=True, default=0)
    isitduration = models.BooleanField('isitduration', default=True ) #eğer set değlide saniye şeklindeyse...
    video = models.TextField(max_length=1000,blank=True , null=True)
    def __str__(self):
        return u'Program Liste : %s ' % (self.name_tr) 

class DietCategory(models.Model):
    name_tr = models.TextField(max_length=1000,blank=True , null=True)
    name_en = models.TextField(max_length=1000,blank=True , null=True)
    explain_tr = models.TextField(max_length=1000,blank=True , null=True)
    explain_en = models.TextField(max_length=1000,blank=True , null=True)    
    image = models.TextField(max_length=1000,blank=True , null=True)
    def __str__(self):
        return u'kategori Ismi : %s ' % (self.name_tr)


class DietSubCategory(models.Model):
    name_en = models.TextField(max_length=1000,blank=True , null=True)
    name_tr = models.TextField(max_length=1000,blank=True , null=True)
    explain_en = models.TextField(max_length=1000,blank=True , null=True)
    explain_tr = models.TextField(max_length=1000,blank=True , null=True)
    Ctgry = models.ForeignKey(DietCategory,blank=True, on_delete=models.CASCADE  , null=True)
    image = models.TextField(max_length=1000,blank=True , null=True)
    totaltime = models.TextField(max_length=1000,blank=True , null=True)
    isitpremium = models.BooleanField('premium')
    def __str__(self):
        return u'Alt Kategori Ismi : %s ' % (self.name_tr)


class DietProgramlist(models.Model):
    name_tr = models.TextField(max_length=1000,blank=True , null=True)
    psc = models.ForeignKey(DietSubCategory, on_delete=models.CASCADE, blank=False , null=False)
    kalori = models.IntegerField(blank=True , null=True)
    ara1 = models.TextField(max_length=1000,blank=True , null=True)
    bfast = models.TextField(max_length=1000,blank=True , null=True)
    ara2 = models.TextField(max_length=1000,blank=True , null=True)
    lunch = models.TextField(max_length=1000,blank=True , null=True)
    ara3= models.TextField(max_length=1000,blank=True , null=True)
    dinner = models.TextField(max_length=1000,blank=True , null=True)
    ara4 = models.TextField(max_length=1000,blank=True , null=True)

    def __str__(self):
        return u'Program Liste : %s ' % (self.name_tr) 

class Form_test(models.Model):
    name_test = models.TextField(max_length=1000,blank=True , null=True)
    explain_test = models.TextField(max_length=1000,blank=True , null=True)
    def __unicode__(self):
        return u'Category name : %s ' % (self.id)
