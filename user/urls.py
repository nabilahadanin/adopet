from django.urls import path
from . import views

app_name = 'user'

urlpatterns = [
    path('form-request-open-donasi/', views.form_request_open_donasi, name='form_request_open_donasi'),
    path('detail-donasi/', views.detail_donasi, name='detail_donasi'),
    path('melakukan-donasi/', views.melakukan_donasi, name='melakukan_donasi'),
    path('form-open-adopt/', views.form_open_adopt, name='form_open_adopt'),
    path('detail-open-adopt/', views.detail_open_adopt, name='detail_open_adopt'),
    path('detail-open-adopt/form-pengadopsian/', views.form_pengadopsian, name='form_pengadopsian'),
    path('profil/', views.profil, name='profil'),
    path('form-request-artikel/', views.form_request_artikel, name='form_request_artikel'),
    path('', views.beranda, name='beranda'),
    path('berhasil-unggah/', views.berhasil_unggah, name='berhasil_unggah'),
    path('berhasil-request/', views.berhasil_request, name='berhasil_request'),
    path('detail-artikel/', views.detail_artikel, name='detail_artikel'),
    path('profil/buat-testimoni/', views.buat_testimoni, name='buat_testimoni'),
    path('chatpage/', views.chatpage, name='chatpage'),
    path('search/', views.searchpage, name='searchpage'),
]
