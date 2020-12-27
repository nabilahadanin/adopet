from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.http import JsonResponse
from django.conf import settings
import copy

from .forms import FormAdopt, FormFoto, FormRequestAdopsi, FormDonasi, FormRequestArtikel, FormTestimoni, FormForum, FormPendonasian
from .models import Hewan, FotoHewan, RequestAdopsi, Donasi, Artikel, Testimoni, Forum, Pendonasian
from adminadopet.models import PostDonasi

response = {}
def form_open_adopt(request):
    form = FormAdopt(request.POST)
    database = Hewan.objects.all()
    if request.method == 'POST':
        response['nama_hewan'] = request.POST['nama_hewan']
        response['jenis_hewan'] = request.POST['jenis_hewan']
        response['jenis_kelamin_hewan'] = request.POST['jenis_kelamin_hewan']
        response['usia_hewan'] = request.POST['usia_hewan']
        response['domisili_hewan'] = request.POST['domisili_hewan']
        response['keterangan'] = request.POST['keterangan']
        response['kategori'] = request.POST['kategori']
        response['kondisi_fisik_hewan'] = request.POST['kondisi_fisik_hewan']
        response['kondisi_psikis_hewan'] = request.POST['kondisi_psikis_hewan']
        response['mahar_adopsi'] = request.POST['mahar_adopsi']
        data = Hewan(nama_hewan = response['nama_hewan'], jenis_hewan = response['jenis_hewan'], jenis_kelamin_hewan = response['jenis_kelamin_hewan'], usia_hewan = response['usia_hewan'], domisili_hewan = response['domisili_hewan'], keterangan = response['keterangan'], kategori = response['kategori'], kondisi_fisik_hewan = response['kondisi_fisik_hewan'], kondisi_psikis_hewan = response['kondisi_psikis_hewan'], mahar_adopsi = response['mahar_adopsi'])
        data.save()
        form = FormAdopt()
        database = Hewan.objects.all()
        return render(request, 'warning/berhasil-unggah.html', {'database': database})
    if request.method == 'DELETE':
        if 'DeleteAll' in request.DELETE:
            Hewan.objects.all().delete()
            context = {
                'form' : form,
                'database' : database
            }
            return render(request, 'openadopt/detail-open-adopt.html', context)
    else:
        form = FormAdopt()
        context = {
            'form' : form,
            'database' : database
        }
        return render(request, 'openadopt/form-open-adopt.html', context)

def detail_open_adopt(request, id):
    forum = Forum.objects.all() 
    hewan = Hewan.objects.get(id = id)
    args = {'hewan' : hewan, 'forum' : forum}
    return render(request, 'openadopt/detail-open-adopt.html', args)

def beranda(request):
    database = Hewan.objects.all().values()
    donasi = Donasi.objects.all().values()
    artikel = Artikel.objects.all().values()
    context = {
        'database' : database, 
        'donasi' : donasi,
        'artikel' : artikel
    }
    return render(request, 'homepage/beranda.html', context)
    
def search(request):
    searchkey = request.GET.get('search')
    database = Hewan.objects.filter(nama_hewan__icontains = searchkey)
    donasi = Donasi.objects.filter(nama_hewan__icontains = searchkey)
    artikel = Artikel.objects.filter(judul_artikel__icontains = searchkey)
    context = {
        'database' : database, 
        'donasi' : donasi,
        'artikel' : artikel
    }
    return render(request, 'homepage/beranda.html', context)

def list_hewan(request):
    hewan_list = list(Hewan.objects.values())
    return JsonResponse(hewan_list, safe=False)

def list_foto(request):
    foto_list = list(FotoHewan.objects.values())
    for i in range(len(foto_list)):
        photo_list[i]['foto'] = settings.MEDIA_URL + foto_list[i]['foto']
    return JsonResponse(foto_list, safe=False)

def form_pengadopsian(request, id):
    form = FormRequestAdopsi(request.POST)
    pengadopsian = RequestAdopsi.objects.all()
    if request.method == 'POST':
        database = Hewan.objects.get(id = id)
        response['id_hewan'] = id
        response['nama_hewan'] = database.nama_hewan
        response['nama_pengadopsi'] = request.POST['nama_pengadopsi']
        response['nomor_hp'] = request.POST['nomor_hp']
        response['email_pengadopsi'] = request.POST['email_pengadopsi']
        response['alamat_pengadopsi'] = request.POST['alamat_pengadopsi']
        data = RequestAdopsi(
            id_hewan = response['id_hewan'],
            nama_hewan = response['nama_hewan'],
            nama_pengadopsi = response['nama_pengadopsi'],
            nomor_hp = response['nomor_hp'],
            email_pengadopsi = response['email_pengadopsi'],
            alamat_pengadopsi = response['alamat_pengadopsi'],
        )
        data.save()
        Form = FormRequestAdopsi() 
        return render(request, 'warning/berhasil-unggah.html', {'database': database, 'pengadopsian': pengadopsian})
    else:
        hewan = Hewan.objects.get(id = id)
        form = FormRequestAdopsi()
        context = {
            'form' : form,
            'hewan' : hewan
        }
        return render(request, 'openadopt/form-pengadopsian.html', context)

def detail_pengadopsian(request, id):
    hewan = Hewan.objects.get(id = id)
    pengadopsian = RequestAdopsi.objects.all().values()
    return render(request, 'openadopt/detail-pengadopsian.html', {'pengadopsian' : pengadopsian, 'hewan' : hewan})

def delete_request_adopsi(request, id_hewan, id_adopsi):
    adopsi = RequestAdopsi.objects.get(id = id_adopsi)
    hewan = Hewan.objects.get(id = id_hewan)
    adopsi.delete()
    pengadopsian = RequestAdopsi.objects.all().values()
    return render(request, 'openadopt/detail-pengadopsian.html', {'pengadopsian' : pengadopsian, 'hewan' : hewan})

def berhasil_adopsi(request, id_hewan, id_adopsi):
    adopsi = RequestAdopsi.objects.get(id = id_adopsi)
    hewan = Hewan.objects.get(id = id_hewan)
    adopsi.delete()
    pengadopsian = RequestAdopsi.objects.all().values()
    return render(request, 'openadopt/detail-pengadopsian.html', {'pengadopsian' : pengadopsian, 'hewan' : hewan})

def form_request_open_donasi(request):
    form = FormDonasi(request.POST)
    database = Donasi.objects.all()
    if request.method == 'POST':
        response['nama_hewan'] = request.POST['nama_hewan']
        response['jenis_hewan'] = request.POST['jenis_hewan']
        response['jenis_kelamin_hewan'] = request.POST['jenis_kelamin_hewan']
        response['usia_hewan'] = request.POST['usia_hewan']
        response['domisili_hewan'] = request.POST['domisili_hewan']
        response['keterangan'] = request.POST['keterangan']
        response['kategori'] = request.POST['kategori']
        response['kondisi_kesehatan'] = request.POST['kondisi_kesehatan']
        response['lokasi_perawatan'] = request.POST['lokasi_perawatan']
        response['biaya_perawatan'] = request.POST['biaya_perawatan']
        data = Donasi(nama_hewan = response['nama_hewan'], jenis_hewan = response['jenis_hewan'], jenis_kelamin_hewan = response['jenis_kelamin_hewan'], usia_hewan = response['usia_hewan'], domisili_hewan = response['domisili_hewan'], keterangan = response['keterangan'], kategori = response['kategori'], kondisi_kesehatan = response['kondisi_kesehatan'], lokasi_perawatan = response['lokasi_perawatan'], biaya_perawatan = response['biaya_perawatan'])
        data.save()
        form = FormDonasi()
        database = Donasi.objects.all()
        return render(request, 'warning/berhasil-request.html', {'database': database})
    if request.method == 'DELETE':
        if 'DeleteAll' in request.DELETE:
            Donasi.objects.all().delete()
            context = {
                'form' : form,
                'database' : database
            }
            return render(request, 'opendonasi/form-request-open-donasi.html', context)
    else:
        form = FormDonasi()
        context = {
            'form' : form,
            'database' : database
        }
        return render(request, 'opendonasi/form-request-open-donasi.html', context)

def detail_donasi(request, id):
    donasi = Donasi.objects.get(id = id)
    args = {'donasi' : donasi}
    return render(request, 'opendonasi/detail-open-donasi.html', args)
    
def melakukan_donasi(request, id):
    form = FormPendonasian(request.POST)
    pendonasian = Pendonasian.objects.all()
    if request.method == 'POST':
        database = Donasi.objects.get(id = id)
        response['id_donasi'] = id
        response['nominal_donasi'] = request.POST['nominal_donasi']
        response['nama_pendonasi'] = request.POST['nama_pendonasi']
        response['metode_donasi'] = request.POST['metode_donasi']
        response['hp_email'] = request.POST['hp_email']
        response['dukungan'] = request.POST['dukungan']
        data = Pendonasian(
            id_donasi = response['id_donasi'],
            nominal_donasi = response['nominal_donasi'],
            nama_pendonasi = response['nama_pendonasi'],
            metode_donasi = response['metode_donasi'],
            hp_email = response['hp_email'],
            dukungan = response['dukungan'],
        )
        data.save()
        Form = FormPendonasian() 
        return render(request, 'warning/berhasil-unggah.html', {'database' : database, 'pendonasian': pendonasian})
    else:
        donasi = Donasi.objects.get(id = id)
        form = FormPendonasian()
        context = {
            'form' : form,
            'donasi' : donasi
        }
        return render(request, 'opendonasi/melakukandonasi.html', context)

def list_donasi(request, id):
    donasi = Donasi.objects.get(id = id)
    pendonasian = Pendonasian.objects.all().values()
    return render(request, 'opendonasi/list-donasi.html', {'pendonasian' : pendonasian, 'donasi' : donasi})

def delete_pendonasian(request, id_donasi, id_pendonasian):
    hasildonasi = Pendonasian.objects.get(id = id_pendonasian)
    donasi = Donasi.objects.get(id = id_donasi)
    hasildonasi.delete()
    pendonasian = Pendonasian.objects.all().values()
    return render(request, 'opendonasi/list-donasi.html', {'pendonasian' : pendonasian, 'donasi' : donasi})

def berhasil_donasi(request, id_donasi, id_pendonasian):
    hasildonasi = Pendonasian.objects.get(id = id_pendonasian)
    donasi = Donasi.objects.get(id = id_donasi)
    hasildonasi.delete()
    pendonasian = Pendonasian.objects.all().values()
    return render(request, 'opendonasi/list-donasi.html', {'pendonasian' : pendonasian, 'donasi' : donasi})

def profil(request):
    testimoni = Testimoni.objects.all().values()
    context = { 'testimoni' : testimoni }
    return render(request, 'profil/profil.html', context)

def form_request_artikel(request):
    form = FormRequestArtikel(request.POST)
    database = Artikel.objects.all()
    if request.method == 'POST':
        response['judul_artikel'] = request.POST['judul_artikel']
        response['isi_artikel'] = request.POST['isi_artikel']
        response['tag_artikel'] = request.POST['tag_artikel']
        data = Artikel(judul_artikel = response['judul_artikel'], isi_artikel = response['isi_artikel'], tag_artikel = response['tag_artikel'])
        data.save()
        form = FormRequestArtikel()
        database = Artikel.objects.all()
        return render(request, 'warning/berhasil-request.html', {'database': database})
    if request.method == 'DELETE':
        if 'DeleteAll' in request.DELETE:
            Artikel.objects.all().delete()
            context = {
                'form' : form,
                'database' : database
            }
            return render(request, 'artikel/form-request-artkel.html', context)
    else:
        form = FormRequestArtikel()
        context = {
            'form' : form,
            'database' : database
        }
        return render(request, 'artikel/form-request-artikel.html', context)

def detail_artikel(request, id):
    artikel = Artikel.objects.get(id = id)
    args = {'artikel' : artikel}
    return render(request, 'artikel/detailartikel.html', args)

def berhasil_request(request):
    return render(request, 'warning/berhasil-request.html')

def berhasil_unggah(request):
    return render(request, 'warning/berhasil-unggah.html')

def buat_testimoni(request):
    form = FormTestimoni(request.POST)
    database = Testimoni.objects.all()
    if request.method == 'POST':
        response['nama_user'] = request.POST['nama_user']
        response['nilai_user'] = request.POST['nilai_user']
        response['komentar_user'] = request.POST['komentar_user']
        data = Testimoni(nama_user = response['nama_user'], nilai_user = response['nilai_user'], komentar_user = response['komentar_user'])
        data.save()
        form = FormAdopt()
        return render(request, 'warning/berhasil-unggah.html', {'database': database})
    if request.method == 'DELETE':
        if 'DeleteAll' in request.DELETE:
            Testimoni.objects.all().delete()
            context = {
                'form' : form,
                'database' : database
            }
            return render(request, 'profil/profil.html', context)
    else:
        form = FormTestimoni()
        context = {
            'form' : form,
            'database' : database
        }
        return render(request, 'profil/form-testimoni.html', context)

def buat_forum(request, id):
    form = FormForum(request.POST)
    forum = Forum.objects.all()
    hewan = Hewan.objects.get(id = id)
    if request.method == 'POST':
        response['id_adopt'] = id
        response['judul_forum'] = request.POST['judul_forum']
        response['isi_forum'] = request.POST['isi_forum']
        data = Forum(judul_forum = response['judul_forum'], isi_forum = response['isi_forum'])
        data.save()
        form = FormForum()
        forum = Forum.objects.all()
        return render(request, 'openadopt/detail-open-adopt.html', {'forum': forum, 'hewan': hewan})
    if request.method == 'DELETE':
        if 'DeleteAll' in request.DELETE:
            Forum.objects.all().delete()
            context = {
                'form' : form,
                'forum' : forum
            }
            return render(request, 'profil/profil.html', context)
    else:
        form = FormForum()
        context = {
            'form' : form,
            'forum' : forum,
        }
        return render(request, 'openadopt/buat-forum.html', context)


def chatpage(request):
    return render(request, 'chatting/chatpage.html')
