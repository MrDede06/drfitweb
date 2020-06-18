from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import *
from django.contrib.admin.views.decorators import staff_member_required
from django.views.decorators.csrf import csrf_exempt
import uuid , json , string , random, urllib, base64, os, sys
from django.utils.encoding import smart_str
from django.core.files.storage import FileSystemStorage

app_name = "backend"

@staff_member_required
@csrf_exempt
def kategori_ekle(request):
    if request.method == 'GET':
        return render(request = request,
                  template_name='spor_kategori_ekle.html')
    data = {}
    if request.method == 'POST':
        
        trkateisim = request.POST.get('trkateisim')
        trkateaciklama = request.POST.get('trkateaciklama')

        enkateisim = request.POST.get('enkateisim')
        enkateaciklama = request.POST.get('enkateaciklama')

  
        myfile2 = request.FILES['myfile']
        fs = FileSystemStorage()
        filename = fs.save(myfile2.name, myfile2)
        print (filename)
        print(trkateisim)
        print(trkateaciklama)
        print(enkateisim)
        print(enkateaciklama)



@staff_member_required
def altkategori_ekle(request):
    return render(request = request,
                  template_name='spor_altkategori_ekle.html')

@csrf_exempt
def addcategoryfy(request):
    data = {}
    if request.method == 'POST':
        
        trkateisim = request.POST.get('trkateisim')
        trkateaciklama = request.POST.get('trkateaciklama')

        enkateisim = request.POST.get('enkateisim')
        enkateaciklama = request.POST.get('enkateaciklama')

        filez = request.POST.get('file')
        print (request.POST)
        print (filez)

        if trkateisim and filez:
            filej = json.loads(filez)
            ftype =  filej['input']['type']
            imgstring = filej['output']['image']
            mylist = imgstring.split(',')
            getjpgorpng = ftype.split('/')
            imgdata = base64.b64decode(mylist[1])
            random_img_name = id_generator(22, "qwertyuopasdfghjklizxcvbnm1234567890")
            filename = '/opt/venv/drfit/drfit/templates/media_cdn/'+random_img_name+'.'+getjpgorpng[1]+''  # I assume you have a way of picking unique filenames
            filenamefordatabase = ''+random_img_name+'.'+getjpgorpng[1]+''
            with open(filename, 'wb') as f:
                f.write(imgdata)
            try:
                getcategory = Category.objects.get(name_tr=trkateisim)
            except Category.DoesNotExist:
                savecate = Category(name_en=enkateisim,
                name_tr=trkateisim,
                explain_en=enkateaciklama,
                explain_tr = trkateaciklama,
                image=filenamefordatabase)
                savecate.save()
                data["message"] = "Great"
                data['response'] = "ok"
                data["filename"] = filenamefordatabase
                return HttpResponse(json.dumps(data), content_type = "application/json")
            data = {"response":"Bu kategori zaten var"}
            return HttpResponse(json.dumps(data), content_type = "application/json")
        else:
            data['response'] = "non"
            data["message"] = "Boş yer bırakmayın"
            return HttpResponse(json.dumps(data), content_type = "application/json")
    else:
        data["message"] = "POST RQ ONLY"
        data["response"] = "non"
        return HttpResponse(json.dumps(data), content_type = "application/json")


@csrf_exempt
def form_test(request):
    if request.method == 'GET':
         return render(request = request,
                  template_name='form_test.html')
    
    if request.method == 'POST':
        var1 = request.POST["trkateisim"]
        var2 = request.POST["trkateaciklama"]
        print (var1)
        print (var2)
     