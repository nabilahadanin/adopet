from django.urls import path
from . import views

app_name = 'user'

urlpatterns = [
    path('form-request-open-donasi/', views.form_request_open_donasi, name='form_request_open_donasi'),
    path('form-open-adopt/', views.form_open_adopt, name='form_open_adopt'),
    path('profil/', views.profil, name='profil'),
    path('buat-artikel/', views.buat_artikel, name='buat_artikel'),
    path('', views.beranda, name='beranda'),
]
