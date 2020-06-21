from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import *
from django.contrib.admin.views.decorators import staff_member_required
from django.views.decorators.csrf import csrf_exempt
import uuid , json , string , random, urllib, base64, os, sys
from django.utils.encoding import smart_str
from django.core.files.storage import FileSystemStorage
from azure.storage.blob import BlobServiceClient, BlobClient

app_name = "backend"

#TODO
path = r"C:\Users\KG672AV\Desktop\DrFit\repos\myenv\drfitweb"
string= "DefaultEndpointsProtocol=https;AccountName=drfitstorage;AccountKey=ueV0MNXhWxVWv9Uh+pJMCuB1gPrac+piwdshUeDcqZ06bf3M8/DOaIAHFwyLc+LXZQVAagkt5CI4lDJi0DBgXQ==;EndpointSuffix=core.windows.net"
#TODO END


@staff_member_required
@csrf_exempt
def kategori_ekle(request):
    data = {}
    
    if request.method == 'GET':
        return render(request = request,
                  template_name='spor_kategori_ekle.html')
    
    if request.method == 'POST':
        
        trkateisim = request.POST.get('trkateisim')
        trkateaciklama = request.POST.get('trkateaciklama')

        enkateisim = request.POST.get('enkateisim')
        enkateaciklama = request.POST.get('enkateaciklama')
 
        filez = request.FILES['myfile']
        fs = FileSystemStorage()
        filename = fs.save(filez.name, filez)
                
        newBasename = "sporKategory" + trkateisim + ".jpg"
        newname = os.path.join(path, newBasename)        
        oldname = os.path.join(path, filename)
        os.rename(oldname, newname)
        
        blob = BlobClient.from_connection_string(container_name="drfitcontainer", conn_str=string, blob_name=newBasename)
        with open(newname, "rb") as data:
            blob.upload_blob(data)
        
        os.remove(newname)     
    


@staff_member_required
def altkategori_ekle(request):
    return render(request = request,
                  template_name='spor_altkategori_ekle.html')




