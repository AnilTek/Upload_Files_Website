from django.shortcuts import render,redirect
from .models import Documents
from django.contrib.auth.decorators import login_required
from . import forms
from django.contrib import messages
import os

# Create your views here.

#is_files_uploaded = {'calisma_ruhsati':False,'faaliyet_belgesi':False,'imza_sirkuleri':False,'oda_kayit_belgesi':False,'kurulus_sozlesmesi':False,'sirketin_mali_bilgileri':False,'ticaret_sicil_odasi':False,'ticaret_sicil_tasdiknamesi':False,'vergi_levhasi':False,'yetki_belgesi':False}

def home(request):
    
    return render(request, 'upload/home.html')

def documents(request):
    document, created = Documents.objects.get_or_create(Sirket_adi=request.user)
   

    document = Documents.objects.get(Sirket_adi=request.user)

    is_files_uploaded = {
    'calisma_ruhsati': bool(document.Calisma_ruhsati_izinler and document.Calisma_ruhsati_izinler.name), 
    'faaliyet_belgesi': bool(document.Faaliyet_belgesi and document.Faaliyet_belgesi.name),
    'imza_sirkuleri': bool(document.Imza_sirkuleri and document.Imza_sirkuleri.name),
    'oda_kayit_belgesi': bool(document.Oda_kayit_belgesi and document.Oda_kayit_belgesi.name),
    'kurulus_sozlesmesi': bool(document.Kurulus_sozlemesi and document.Kurulus_sozlemesi.name),
    'sirketin_mali_bilgileri': bool(document.Sirketin_mali_bilgileri and document.Sirketin_mali_bilgileri.name),
    'ticaret_sicil_odasi': bool(document.Ticaret_sicil_gazetesi and document.Ticaret_sicil_gazetesi.name),
    'ticaret_sicil_tasdiknamesi': bool(document.Ticaret_sicil_tasdiknamesi and document.Ticaret_sicil_tasdiknamesi.name),
    'vergi_levhasi': bool(document.Vergi_levhasi and document.Vergi_levhasi.name),
    'yetki_belgesi': bool(document.Yetki_belgesi and document.Yetki_belgesi.name),
}
    
    print(is_files_uploaded)


    all_files_uploaded = all(is_files_uploaded.values())


    


  


    return render(request, 'upload/documents.html' , {'is_files_uploaded': is_files_uploaded , 'all_files_uploaded': all_files_uploaded})

#--------------------------------------------------------------------------------------------------------
@login_required(login_url='/users/documents')
def calisma_ruhsati(request):
    file = None
    is_uploaded = False
    try:
        document = Documents.objects.get(Sirket_adi=request.user)
    except Documents.DoesNotExist:
        document = Documents(Sirket_adi=request.user)  # Hazli hazirda dosya yoksa yeni dosya olusturur

    # Varolan Dosyayi silme 
    if request.method == 'POST' and request.POST.get('action') == 'clear':
        document.Calisma_ruhsati_izinler.delete(save=True)
        messages.success(request, "Dosya Basari ile olusturuldu")
        print(request.user)
        

    # Dosya Yukleme
    if request.method == 'POST' and request.POST.get('action') == 'submit' :
        form = forms.Calisma_ruhsati_izinler(request.POST, request.FILES, instance=document)
        print(request.FILES)  # Check if the file is being sent
        print(form.errors)



        if form.is_valid():  
            form.save()
            file = document.Calisma_ruhsati_izinler.name
            
        else:
            messages.error(request, "Yukleme esnasinda bir problem olustu")

    


    else:
        form = forms.Calisma_ruhsati_izinler(instance=document)


    if document.Calisma_ruhsati_izinler:
        is_uploaded = True

    return render(request, 'upload/calisma_ruhsati.html', context= {'form':form ,'file':file,'is_uploaded':is_uploaded })



#--------------------------------------------------------------------------------------------------------
@login_required(login_url='/users/documents')
def faaliyet_belgesi(request):
    file = None
    is_uploaded = False
    try:
        document = Documents.objects.get(Sirket_adi=request.user)
    except Documents.DoesNotExist:
        document = Documents(Sirket_adi=request.user)  

    
    if request.method == 'POST' and request.POST.get('action') == 'clear':
        document.Faaliyet_belgesi.delete()
        document.save()
        messages.success(request, "Dosya Basari ile olusturuldu")
        print(request.user)
        

    
    if request.method == 'POST' and request.POST.get('action') == 'submit':
        form = forms.Faaliyet_belgesi(request.POST, request.FILES, instance=document)
        print(request.FILES)  
        print(form.errors)

        if form.is_valid():
            form.save()
            file = document.Faaliyet_belgesi.name
            
            
        else:
             messages.error(request, "Yukleme esnasinda bir problem olustu")
    else:
        form = forms.Faaliyet_belgesi(instance=document)
    
    if document.Faaliyet_belgesi:
        is_uploaded = True

    return render(request, 'upload/faaliyet_belgesi.html', context= {'form':form,'file':file,'is_uploaded':is_uploaded})
#--------------------------------------------------------------------------------------------------------


@login_required(login_url='/users/documents')
def imza_sirkuleri(request):
    file = None
    is_uploaded = False
    try:
        document = Documents.objects.get(Sirket_adi=request.user)
    except Documents.DoesNotExist:
        document = Documents(Sirket_adi=request.user)  

    
    if request.method == 'POST' and request.POST.get('action') == 'clear':
        document.Imza_sirkuleri.delete()
        document.save()
        messages.success(request, "Dosya Basari ile olusturuldu")
        print(request.user)
        

    
    if request.method == 'POST' and request.POST.get('action') == 'submit':
        form = forms.Imza_sirkuleri(request.POST, request.FILES, instance=document)
        print(request.FILES)  
        print(form.errors)

        if form.is_valid():
            form.save()
            file = document.Imza_sirkuleri.name
            
            
        else:
             messages.error(request, "Yukleme esnasinda bir problem olustu")
    else:
        form = forms.Imza_sirkuleri(instance=document)

    if document.Imza_sirkuleri:
        is_uploaded = True

    return render(request, 'upload/imza_sirkuleri.html', context= {'form':form,'file':file,'is_uploaded':is_uploaded})

#--------------------------------------------------------------------------------------------------------
@login_required(login_url='/users/documents')
def oda_kayit_belgesi(request):
    file = None
    is_uploaded = False
    try:
        document = Documents.objects.get(Sirket_adi=request.user)
    except Documents.DoesNotExist:
        document = Documents(Sirket_adi=request.user)  

    
    if request.method == 'POST' and request.POST.get('action') == 'clear':
        document.Oda_kayit_belgesi.delete()
        document.save()
        messages.success(request, "Dosya Basari ile olusturuldu")
        print(request.user)
        

    
    if request.method == 'POST' and request.POST.get('action') == 'submit':
        form = forms.Oda_kayit_belgesi(request.POST, request.FILES, instance=document)
        print(request.FILES)  
        print(form.errors)

        if form.is_valid():
            form.save()
            file = document.Oda_kayit_belgesi.name
            
            
        else:
            messages.error(request, "Yukleme esnasinda bir problem olustu")
    else:
        form = forms.Oda_kayit_belgesi(instance=document)

    if document.Oda_kayit_belgesi:
        is_uploaded = True
    return render(request, 'upload/oda_kayit_belgesi.html', context= {'form':form,'file':file,'is_uploaded':is_uploaded})
#--------------------------------------------------------------------------------------------------------

@login_required(login_url='/users/documents')
def kurulus_sozlesmesi(request):
    file = None
    is_uploaded = False
    try:
        document = Documents.objects.get(Sirket_adi=request.user)
    except Documents.DoesNotExist:
        document = Documents(Sirket_adi=request.user)  

    
    if request.method == 'POST' and request.POST.get('action') == 'clear':
        document.Kurulus_sozlemesi.delete()
        document.save()
        messages.success(request, "Dosya Basari ile olusturuldu")
        print(request.user)
        

    
    if request.method == 'POST' and request.POST.get('action') == 'submit':
        form = forms.Kurulus_sozlemesi(request.POST, request.FILES, instance=document)
        print(request.FILES)  
        print(form.errors)

        if form.is_valid():
            form.save()
            file = document.Kurulus_sozlemesi.name
            
            
        else:
            messages.error(request, "Yukleme esnasinda bir problem olustu")
    else:
        form = forms.Kurulus_sozlemesi(instance=document)

    if document.Kurulus_sozlemesi:
        is_uploaded = True

    return render(request, 'upload/kurulus_sozlesmesi.html', context= {'form':form,'file':file,'is_uploaded':is_uploaded})

#--------------------------------------------------------------------------------------------------------
@login_required(login_url='/users/documents')
def sirketin_mali_bilgileri(request):
    file = None
    is_uploaded = False
    try:
        document = Documents.objects.get(Sirket_adi=request.user)
    except Documents.DoesNotExist:
        document = Documents(Sirket_adi=request.user)  

    
    if request.method == 'POST' and request.POST.get('action') == 'clear':
        document.Sirketin_mali_bilgileri.delete()
        document.save()
        messages.success(request, "Dosya Basari ile olusturuldu")
        print(request.user)
        

    
    if request.method == 'POST' and request.POST.get('action') == 'submit':
        form = forms.Sirketin_mali_bilgileri(request.POST, request.FILES, instance=document)
        print(request.FILES)  
        print(form.errors)

        if form.is_valid():
            form.save()
            file = document.Sirketin_mali_bilgileri.name
            
            
        else:
            messages.error(request, "Yukleme esnasinda bir problem olustu")
    else:
        form = forms.Sirketin_mali_bilgileri(instance=document)

    if document.Sirketin_mali_bilgileri:
        is_uploaded = True


    return render(request, 'upload/sirketin_mali_bilgileri.html', context= {'form':form,'file':file,'is_uploaded':is_uploaded})
#--------------------------------------------------------------------------------------------------------

@login_required(login_url='/users/documents')
def ticaret_sicil_odasi(request):
    file = None
    is_uploaded = False
    try:
        document = Documents.objects.get(Sirket_adi=request.user)
    except Documents.DoesNotExist:
        document = Documents(Sirket_adi=request.user) 

    
    if request.method == 'POST' and request.POST.get('action') == 'clear':
        document.Ticaret_sicil_gazetesi.delete()
        document.save()
        messages.success(request, "Dosya Basari ile olusturuldu")
        print(request.user)
        

   
    if request.method == 'POST' and request.POST.get('action') == 'submit':
        form = forms.Ticaret_sicil_gazetesi(request.POST, request.FILES, instance=document)
        print(request.FILES)  
        print(form.errors)

        if form.is_valid():
            form.save()
            file = document.Ticaret_sicil_gazetesi.name
            messages.success(request, "Çalışma Ruhsatı ve İzinler successfully uploaded.")
            
        else:
            messages.error(request, "Yukleme esnasinda bir problem olustu")
    else:
        form = forms.Ticaret_sicil_gazetesi(instance=document)

    if document.Ticaret_sicil_gazetesi:
        is_uploaded = True

    return render(request, 'upload/ticaret_sicil_odasi.html', context= {'form':form,'file':file,'is_uploaded':is_uploaded})
#--------------------------------------------------------------------------------------------------------

@login_required(login_url='/users/documents')
def ticaret_sicil_tasdiknamesi(request):
    file = None
    is_uploaded = False
    try:
        document = Documents.objects.get(Sirket_adi=request.user)
    except Documents.DoesNotExist:
        document = Documents(Sirket_adi=request.user)  

    
    if request.method == 'POST' and request.POST.get('action') == 'clear':
        document.Ticaret_sicil_tasdiknamesi.delete()
        document.save()
        messages.success(request, "Dosya Basari ile olusturuldu")
        print(request.user)
        

    
    if request.method == 'POST' and request.POST.get('action') == 'submit':
        form = forms.Ticaret_sicil_tasdiknamesi(request.POST, request.FILES, instance=document)
        print(request.FILES)  
        print(form.errors)

        if form.is_valid():
            form.save()
            file = document.Ticaret_sicil_tasdiknamesi.name
            
            
        else:
            messages.error(request, "Yukleme esnasinda bir problem olustu")
    else:
        form = forms.Ticaret_sicil_tasdiknamesi(instance=document)

    if document.Ticaret_sicil_tasdiknamesi:
        is_uploaded = True

    return render(request, 'upload/ticaret_sicil_tasdiknamesi.html', context= {'form':form,'file':file,'is_uploaded':is_uploaded})
#--------------------------------------------------------------------------------------------------------


@login_required(login_url='/users/documents')
def vergi_levhasi(request):
    file = None
    is_uploaded = False
    try:
        document = Documents.objects.get(Sirket_adi=request.user)
    except Documents.DoesNotExist:
        document = Documents(Sirket_adi=request.user)  

    
    if request.method == 'POST' and request.POST.get('action') == 'clear':
        document.Vergi_levhasi.delete()
        document.save()
        messages.success(request, "Dosya Basari ile olusturuldu")
        print(request.user)
        

    
    if request.method == 'POST' and request.POST.get('action') == 'submit':
        form = forms.Vergi_levhasi(request.POST, request.FILES, instance=document)
        print(request.FILES)  
        print(form.errors)

        if form.is_valid():
            form.save()
            file = document.Vergi_levhasi.name
            
            
        else:
            messages.error(request, "Yukleme esnasinda bir problem olustu")
    else:
        form = forms.Vergi_levhasi(instance=document)

    if document.Vergi_levhasi:
        is_uploaded = True


    return render(request, 'upload/vergi_levhasi.html', context= {'form':form,'file':file,'is_uploaded':is_uploaded})

#--------------------------------------------------------------------------------------------------------
@login_required(login_url='/users/documents')
def yetki_belgesi(request):
    file = None
    is_uploaded = False
    try:
        document = Documents.objects.get(Sirket_adi=request.user)
    except Documents.DoesNotExist:
        document = Documents(Sirket_adi=request.user) 

    
    if request.method == 'POST' and request.POST.get('action') == 'clear':
        document.Yetki_belgesi.delete()
        document.save()
        messages.success(request, "File successfully cleared.")
        print(request.user)
        

    
    if request.method == 'POST' and request.POST.get('action') == 'submit':
        form = forms.Yetki_belgesi(request.POST, request.FILES, instance=document)
        print(request.FILES)  
        print(form.errors)

        if form.is_valid():
            form.save()
            file = document.Yetki_belgesi.name
            messages.success(request, "Çalışma Ruhsatı ve İzinler successfully uploaded.")
            
        else:
            messages.error(request, "There was an issue with the upload. Please try again.")
    else:
        form = forms.Yetki_belgesi(instance=document)

    
    if document.Yetki_belgesi:
        is_uploaded = True


    return render(request, 'upload/yetki_belgesi.html', context= {'form':form,'file':file,'is_uploaded':is_uploaded})
#--------------------------------------------------------------------------------------------------------
'''
    calisma_ruhsati = document.Calisma_ruhsati_izinler.name
    faaliyet_belgesi = document.Faaliyet_belgesi.name
    imza_sirkuleri = document.Imza_sirkuleri.name
    oda_kayit_belgesi = document.Oda_kayit_belgesi.name
    kurulus_sozlesmesi = document.Kurulus_sozlemesi.name
    sirketin_mali_bilgileri = document.Sirketin_mali_bilgileri.name
    ticaret_sicil_odasi = document.Ticaret_sicil_gazetesi.name
    ticaret_sicil_tasdiknamesi = document.Ticaret_sicil_tasdiknamesi.name
    vergi_levhasi = document.Vergi_levhasi.name
    yetki_belgesi = document.Yetki_belgesi.name

    print(is_files_uploaded)
    


    if calisma_ruhsati is not '':
        print('Hello')
        print(calisma_ruhsati)
        is_files_uploaded['calisma_ruhsati'] = True

    if faaliyet_belgesi is not '':
        print('Hello')
        print(faaliyet_belgesi)
        is_files_uploaded['faaliyet_belgesi'] = True

    if imza_sirkuleri is not '':
        print('Hello')
        print(imza_sirkuleri)
        is_files_uploaded['imza_sirkuleri'] = True
    
    if oda_kayit_belgesi is not '':
        print('Hello')
        print(oda_kayit_belgesi)
        is_files_uploaded['oda_kayit_belgesi'] = True

    if kurulus_sozlesmesi is not '':
        print('Hello')
        print(kurulus_sozlesmesi)
        is_files_uploaded['kurulus_sozlesmesi'] = True

    if sirketin_mali_bilgileri is not '':
        print('Hello')
        print(sirketin_mali_bilgileri)
        is_files_uploaded['sirketin_mali_bilgileri'] = True

    if ticaret_sicil_odasi is not '':
        print('Hello')
        print(ticaret_sicil_odasi)
        is_files_uploaded['ticaret_sicil_odasi'] = True

    if ticaret_sicil_tasdiknamesi is not '':
        print('Hello')
        print(ticaret_sicil_tasdiknamesi)
        is_files_uploaded['ticaret_sicil_tasdiknamesi'] = True

    if vergi_levhasi is not '':
        print('Hello')
        print(vergi_levhasi)
        is_files_uploaded['vergi_levhasi'] = True

    if yetki_belgesi is not '':
        print('Hello')
        print(yetki_belgesi)
        is_files_uploaded['yetki_belgesi'] = True

'''

def all_files_uploaded(request):
    
    return render(request, 'upload/all_files_uploaded.html')