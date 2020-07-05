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
#container_name leri yarat
#TODO END

@staff_member_required
@csrf_exempt
def kategori_ekle(request):
    if request.method == 'GET':
        getkategoris = Category.objects.all()
        return render(request = request,
                  template_name='diet_kategori.html')   
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
            newBasename = "dietKategory" + trkateisim + str(num) + ".jpg"
            newname = os.path.join(path, newBasename)        
            oldname = os.path.join(path, filename)
            os.rename(oldname, newname)            
            blob = BlobClient.from_connection_string(container_name="diet-kategori", conn_str=string, blob_name=newBasename)                      
            with open(newname, "rb") as data:
                    blob.upload_blob(data)
            try: 
                getcategory = DietCategory.objects.get(name_tr=trkateisim)
                messages.error(request, "Bu Kategori zaten mevcut, baska kategori ekleyin")
            except OSError:
                messages.error(request, "Resim kaydedilemedi tekrar deneyin")
            except DietCategory.DoesNotExist:
                savecate = DietCategory(name_en = enkateisim,
                name_tr = trkateisim,
                explain_en = enkateaciklama,
                explain_tr = trkateaciklama,
                image = newBasename)
                savecate.save()
                messages.success(request, "Kategori Basari ile Kaydedildi")
            os.remove(newname)     
            return render(request = request,
                    template_name='diet_kategori.html')              
        else:
            messages.error(request, "Lutfen Turkce Kategori Ismi Belirleyin")
            return render(request = request,
                    template_name='diet_kategori.html')

@csrf_exempt
@staff_member_required
def altkategori_ekle(request):
    if request.method == 'GET':
        return render(request = request,
                  template_name='diet_altkategori.html',
                  context = {"categories":DietCategory.objects.all})
    if request.method == 'POST':
        try:
            preboool = False
            totaltime = request.POST.get('totaltime')
            trkateisim = request.POST.get('traltkateisim')
            trkateaciklama = request.POST.get('traltkateaciklama')
            enkateisim = request.POST.get('enaltkateisim')
            enkateaciklama = request.POST.get('enaltkateaciklama')
            cname = request.POST.get('dropdown1')
            category = DietCategory.objects.get(name_tr = cname)
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
                newBasename = "dietAltKategory" + trkateisim + str(num) + ".jpg"
                newname = os.path.join(path, newBasename)        
                oldname = os.path.join(path, filename)
                os.rename(oldname, newname)           
                blob = BlobClient.from_connection_string(container_name="diet-altkategori", conn_str=string, blob_name=newBasename)
                category = DietCategory.objects.get(id=categoryid)       
                with open(newname, "rb") as data:
                    blob.upload_blob(data)  
                try: 
                    getsubcategory = DietSubCategory.objects.get(name_tr=trkateisim)
                    messages.error(request, "Bu Alt Kategori zaten mevcut, baska alt kategori ekleyin")    
                    os.remove(newname)  
                except DietSubCategory.DoesNotExist:
                    savesubcate = DietSubCategory(Ctgry=category,
                        totaltime=totaltime,
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
        except DietCategory.DoesNotExist:
            messages.error(request, "Kategori seciniz")              
        
        return render(request = request,
                template_name='diet_altkategori.html',
                context = {"categories":DietCategory.objects.all})              
            

@csrf_exempt
@staff_member_required
def programlist(request):
    if request.method == 'GET':   
        return render(request = request,
                  template_name='diet_programlist.html',
                  context = {"categories":DietCategory.objects.all, "subcategories":DietSubCategory.objects.all})

    if request.method == 'POST':
        
        cnameCategory = request.POST.get('dropdown')
        cnameScategory = request.POST.get('dropdown1')
        cnameKalori = request.POST.get('dropdown2')
        trkateisim = request.POST.get('traltkateisim')
        if (cnameCategory != None) or (cnameScategory != None) or (cnameKalori != None)  or trkateisim:
            try:
                DietProgramlist.objects.get(name_tr = trkateisim)
            except DietProgramlist.DoesNotExist:
                category = DietCategory.objects.get(name_tr = cnameCategory)
                categoryid = category.id       
                subcategory= DietSubCategory.objects.get(name_tr = cnameScategory)
                subcategoryid = subcategory.id
                getsubcate = DietSubCategory.objects.get(id=int(subcategoryid))
                koncesi = request.POST.get('araog1')
                kahvalti = request.POST.get('kahvalti')
                araogun1 = request.POST.get('araog2')
                ogleyemegi = request.POST.get('ogley')
                araogun2 = request.POST.get('araog3')
                aksamyemegi = request.POST.get('aksamy')
                supper = request.POST.get('araog4')
                programlist = DietProgramlist(name_tr=trkateisim,
                        psc=getsubcate,
                        kalori=cnameKalori,
                        ara1=koncesi,
                        bfast=kahvalti,
                        ara2=araogun1,
                        lunch=ogleyemegi,
                        ara3=araogun2,
                        dinner=aksamyemegi,
                        ara4=supper
                        )
                programlist.save()
                messages.success(request, "Program Basari ile Kaydedildi")
            else:
                messages.error(request, "Bu Program zaten var lütfen yeni isim giriniz")

        else:
            messages.error(request, "Türkçe program ismi belirleyin, Kategori seçin, Alt Kategori seçin, Kalori aralığı kısımlarını boş bırakmayınız.")  

        return render(request = request,
                  template_name='diet_programlist.html',
                  context = {"categories":DietCategory.objects.all, "subcategories":DietSubCategory.objects.all})

        