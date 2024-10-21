from django.urls import path
from . import views

app_name = 'upload'

urlpatterns = [
    path('',views.home , name='entry'),
    path('documents' , views.documents,name='documents'),
    path('calisma_ruhsati' , views.calisma_ruhsati,name='calisma_ruhsati'),
    path('faaliyet_belgesi' , views.faaliyet_belgesi,name='faaliyet_belgesi'),
    path('imza_sirkuleri' , views.imza_sirkuleri,name='imza_sirkuleri'),
    path('oda_kayit_belgesi' , views.oda_kayit_belgesi,name='oda_kayit_belgesi'),
    path('kurulus_sozlesmesi' , views.kurulus_sozlesmesi,name='kurulus_sozlesmesi'),
    path('sirketin_mali_bilgileri' , views.sirketin_mali_bilgileri,name='sirketin_mali_bilgileri'),
    path('ticaret_sicil_odasi' , views.ticaret_sicil_odasi,name='ticaret_sicil_odasi'),
    path('ticaret_sicil_tasdiknamesi' , views.ticaret_sicil_tasdiknamesi,name='ticaret_sicil_tasdiknamesi'),
    path('vergi_levhasi' , views.vergi_levhasi,name='vergi_levhasi'),
    path('yetki_belgesi' , views.yetki_belgesi,name='yetki_belgesi'),
    path('all_files_uploaded/', views.all_files_uploaded, name='all_files_uploaded'),
    

    
]
