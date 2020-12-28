from django.urls import path
from . import views

app_name = 'user'

urlpatterns = [
    path('form-request-open-donasi/', views.form_request_open_donasi, name='form_request_open_donasi'),
    path('detail-donasi/<id>/', views.detail_donasi, name='detail_donasi'),
    path('detail-donasi/<id>/melakukan-donasi/', views.melakukan_donasi, name='melakukan_donasi'),
    path('detail-donasi/<id>/list-donasi/', views.list_donasi, name='list_donasi'),
    path('detail-donasi/<id_donasi>/list-donasi/<id_pendonasian>/delete', views.delete_pendonasian, name='delete_pendonasian'),
    path('detail-donasi/<id_donasi>/list-donasi/<id_pendonasian>/berhasil', views.berhasil_donasi, name='berhasil_donasi'),
    path('form-open-adopt/', views.form_open_adopt, name='form_open_adopt'),
    path('detail-open-adopt/<id>/', views.detail_open_adopt, name='detail_open_adopt'),
    path('detail-open-adopt/<id>/buat-forum/', views.buat_forum, name='buat_forum'),
    path('detail-open-adopt/<id_hewan>/forum/<id_forum>/reply/', views.reply_forum, name='reply_forum'),
    path('detail-open-adopt/<id>/form-pengadopsian/', views.form_pengadopsian, name='form_pengadopsian'),
    path('detail-open-adopt/<id>/detail-pengadopsian/', views.detail_pengadopsian, name='detail_pengadopsian'),
    path('detail-open-adopt/<id_hewan>/detail-pengadopsian/<id_adopsi>/delete', views.delete_request_adopsi, name='delete_request_adopsi'),
    path('detail-open-adopt/<id_hewan>/detail-pengadopsian/<id_adopsi>/berhasil', views.berhasil_adopsi, name='berhasil_adopsi'),
    path('profil/', views.profil, name='profil'),
    path('form-request-artikel/', views.form_request_artikel, name='form_request_artikel'),
    path('', views.beranda, name='beranda'),
    path('berhasil-unggah/', views.berhasil_unggah, name='berhasil_unggah'),
    path('berhasil-request/', views.berhasil_request, name='berhasil_request'),
    path('detail-artikel/<id>/', views.detail_artikel, name='detail_artikel'),
    path('profil/buat-testimoni/', views.buat_testimoni, name='buat_testimoni'),
    path('chatpage/', views.chatpage, name='chatpage'),
    path('chatpage/send/<id_pengirim>/<id_penerima>', views.send_message, name='send_message'),
    path('list_hewan/', views.list_hewan, name='list_hewan'),
    path('list_foto/', views.list_foto, name='list_foto'),
    path('search/', views.search, name='search')
]
