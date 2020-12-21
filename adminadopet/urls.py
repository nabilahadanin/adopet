from django.urls import path
from . import views

app_name = 'adminadopet'

urlpatterns = [
    path('', views.beranda, name='beranda'),
    path('eval-open-donasi/<id>/delete', views.delete_open_donasi, name= 'delete_open_donasi'),
    path('eval-open-donasi/<id>/', views.eval_open_donasi, name='eval_open_donasi'),
    path('eval-artikel/<id>/', views.eval_artikel, name='eval_artikel'),
    path('eval-artikel/<id>/delete', views.delete_artikel, name='delete_artikel'),
    path('berhasil-unggah/', views.berhasil_unggah, name="berhasil_unggah"),
    path('search/', views.search, name='search'),
]
