from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import *
from django.contrib.admin.views.decorators import staff_member_required
from django.contrib.auth import  logout

@staff_member_required
def yonetim(request):
    return render(request = request,
                  template_name='yonetim_home.html')


def logout_request(request):
  logout(request)
  return redirect("admin:logout")


@staff_member_required
def spor_main(request):
    return render(request = request,
                  template_name='spor_home.html')

@staff_member_required
def diet_main(request):
    return render(request = request,
                  template_name='diet_home.html')