from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import *
from django.contrib.admin.views.decorators import staff_member_required
from django.views.decorators.csrf import csrf_exempt
import uuid , json , string , random, urllib, base64, os, sys
from django.utils.encoding import smart_str
from django.core.files.storage import FileSystemStorage
from azure.storage.blob import BlobServiceClient, BlobClient, ContainerClient
from django.contrib import messages

app_name = "backend"

#TODO
path = r"C:\Users\KG672AV\Desktop\DrFit\repos\myenv\drfitweb"
string= "DefaultEndpointsProtocol=https;AccountName=drfitstorage;AccountKey=ueV0MNXhWxVWv9Uh+pJMCuB1gPrac+piwdshUeDcqZ06bf3M8/DOaIAHFwyLc+LXZQVAagkt5CI4lDJi0DBgXQ==;EndpointSuffix=core.windows.net"
#TODO END

@staff_member_required
@csrf_exempt
def kategori_ekle(request):
    if request.method == 'GET':
        getkategoris = Category.objects.all()
        return render(request = request,
                  template_name='spor_kategori_ekle.html')   
    if request.method == 'POST':        
        trkateisim = request.POST.get('trkateisim')
        trkateaciklama = request.POST.get('trkateaciklama')
        enkateisim = request.POST.get('enkateisim')
        enkateaciklama = request.POST.get('enkateaciklama')        
        filez = request.FILES['file']
        if trkateisim:
            fs = FileSystemStorage()
            filename = fs.save(filez.name, filez)                    
            num = random.randrange(1, 10**3)
            newBasename = "sporKategory" + trkateisim + str(num) + ".jpg"
            newname = os.path.join(path, newBasename)        
            oldname = os.path.join(path, filename)
            os.rename(oldname, newname)            
            blob = BlobClient.from_connection_string(container_name="spor-kategori", conn_str=string, blob_name=newBasename)                      
            with open(newname, "rb") as data:
                    blob.upload_blob(data)
            try: 
                getcategory = Category.objects.get(name_tr=trkateisim)
                messages.error(request, "Bu Kategori zaten mevcut, baska kategori ekleyin")
            except OSError:
                messages.error(request, "Resim kaydedilemedi tekrar deneyin")
            except Category.DoesNotExist:
                savecate = Category(name_en = enkateisim,
                name_tr = trkateisim,
                explain_en = enkateaciklama,
                explain_tr = trkateaciklama,
                image = newBasename)
                savecate.save()
                messages.success(request, "Kategori Basari ile Kaydedildi")
            os.remove(newname)     
            return render(request = request,
                    template_name='spor_kategori_ekle.html')              
        else:
            messages.error(request, "Lutfen Turkce Kategori Ismi Belirleyin")
            return render(request = request,
                    template_name='spor_kategori_ekle.html')

@csrf_exempt
@staff_member_required
def altkategori_ekle(request):
    if request.method == 'GET':
        return render(request = request,
                  template_name='spor_altkategori_ekle.html',
                  context = {"categories":Category.objects.all})
    if request.method == 'POST':
        try:
            preboool = False
            totaltime = request.POST.get('totaltime')
            trkateisim = request.POST.get('traltkateisim')
            trkateaciklama = request.POST.get('traltkateaciklama')
            enkateisim = request.POST.get('enaltkateisim')
            enkateaciklama = request.POST.get('enaltkateaciklama')
            cname = request.POST.get('dropdown1')
            category = Category.objects.get(name_tr = cname)
            categoryid = category.id
            premium = request.POST.get('premium')        
            if premium:
                preboool = True    
            alanbox = request.POST.get('dropdown2')
            filez = request.FILES['file']            
            if trkateisim:
                fs = FileSystemStorage()
                filename = fs.save(filez.name, filez)                  
                num = random.randrange(1, 10**3)
                newBasename = "sporAltKategory" + trkateisim + str(num) + ".jpg"
                newname = os.path.join(path, newBasename)        
                oldname = os.path.join(path, filename)
                os.rename(oldname, newname)           
                blob = BlobClient.from_connection_string(container_name="spor-altkategori", conn_str=string, blob_name=newBasename)
                category = Category.objects.get(id=categoryid)       
                with open(newname, "rb") as data:
                    blob.upload_blob(data)  
                try: 
                    getsubcategory = SubCategory.objects.get(name_tr=trkateisim)
                    messages.error(request, "Bu Alt Kategori zaten mevcut, baska alt kategori ekleyin")    
                    os.remove(newname)  
                except SubCategory.DoesNotExist:
                    savesubcate = SubCategory(Ctgry=category,
                        totaltime=totaltime,
                        place=alanbox,
                        name_en=enkateisim,
                        name_tr=trkateisim,
                        explain_en=enkateaciklama,
                        explain_tr = trkateaciklama,
                        image=newBasename,
                        isitpremium=preboool)
                    savesubcate.save()
                    messages.success(request, "Alt Kategori Basari ile Kaydedildi")
                    os.remove(newname)
            else:
                messages.error(request, "Lutfen Turkce Kategori Ismi Belirleyin")        
        except Category.DoesNotExist:
            messages.error(request, "Kategori seciniz")              
        
        return render(request = request,
                template_name='spor_altkategori_ekle.html',
                context = {"categories":Category.objects.all})              
            


@staff_member_required
def form_test(request):   
    return render(request = request,
                  template_name='form_test.html',
                  context = {"categories":Category.objects.all})


@staff_member_required
def programlist(request):
    if request.method == 'GET':   
        return render(request = request,
                  template_name='spor_programlist.html',
                  context = {"categories":Category.objects.all, "subcategories":SubCategory.objects.all})

    if request.method == 'POST':
        
        cnameCategory = request.POST.get('dropdown1')
        cnameScategory = request.POST.get('dropdown2')
        trkateisim = request.POST.get('traltkateisim')
        if (cnameCategory != None) or (cnameScategory != None) or trkateisim:

            category = Category.objects.get(name_tr = cnameCategory)
            categoryid = category.id
       
            subcategory= SubCategory.objects.get(name_tr = cnameScategory)
            subcategoryid = subcategory.id
            getsubcate = SubCategory.objects.get(id=int(subcategoryid))
            tekrarsaytisi = request.POST.get('tekrarsayisi')
            setsayisi = request.POST.get('setsayisix')
            resttime = request.POST.get('resttime')
            isitduration = request.POST.get('isitduration')
            filez = request.FILES['file']
            fs = FileSystemStorage()
            filename = fs.save(filez.name, filez)                    
            num = random.randrange(1, 10**3)
            newBasename = "sporKatProgram" + trkateisim + str(num) + ".mp4"
            newname = os.path.join(path, newBasename)        
            oldname = os.path.join(path, filename)
            os.rename(oldname, newname)            
            blob = BlobClient.from_connection_string(container_name="spor-katprogram", conn_str=string, blob_name=newBasename)
            if isitduration:
                preboool = True
            else:
                preboool = False
            with open(newname, "rb") as data:
                blob.upload_blob(data)
            try:
                programlist = Programlist(name_tr=trkateisim,
                    psc=getsubcate,
                    setcount=setsayisi,
                    replycount=tekrarsaytisi,
                    isitduration=preboool,
                    resttime=resttime,
                    video=newBasename
                    )
                programlist.save()
                os.remove(newname)  
                messages.success(request, "Program Basari ile Kaydedildi")
            except OSError:
                messages.error(request, "Video kaydedilemedi tekrar deneyin")

        else:
            messages.error(request, "Program Ismi, Kategori ya da Altkategori Seçmediniz. Lütfen kategori, alt kategori ve program ismi kısımlarını boş bırakmayınız.")  

        return render(request = request,
                  template_name='spor_programlist.html',
                  context = {"categories":Category.objects.all, "subcategories":SubCategory.objects.all})

        