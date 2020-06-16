from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import *
from django.contrib.admin.views.decorators import staff_member_required

app_name = "backend"

@staff_member_required
def kategori_ekle(request):
    return render(request = request,
                  template_name='spor_kategori_ekle.html')

@staff_member_required
def altkategori_ekle(request):
    return render(request = request,
                  template_name='spor_altkategori_ekle.html')