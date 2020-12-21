from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.http import JsonResponse
from django.conf import settings
import copy
from user.forms import FormDonasi
from user.models import Donasi, Artikel

# Create your views here.
response = {}
def beranda(request):
    database = Donasi.objects.all().values()
    post_artikel = Artikel.objects.all().values()
    context = {
        'database' : database,
        'post_artikel' : post_artikel
    }
    return render(request, 'homepage/beranda-admin.html', context)

def eval_open_donasi(request, id):
    donasi = Donasi.objects.get(id = id)
    if request.method == 'POST':
        response['nama_hewan'] = donasi.nama_hewan
        response['jenis_hewan'] = donasi.jenis_hewan
        response['jenis_kelamin_hewan'] = donasi.jenis_kelamin_hewan
        response['usia_hewan'] = donasi.usia_hewan
        response['domisili_hewan'] = donasi.domisili_hewan
        response['keterangan'] = donasi.keterangan
        response['kategori'] = donasi.kategori
        response['kondisi_kesehatan'] = donasi.kondisi_kesehatan
        response['lokasi_perawatan'] = donasi.lokasi_perawatan
        response['biaya_perawatan'] = donasi.biaya_perawatan
        response['verifikasi'] = True
        data = Donasi(id = id, nama_hewan = response['nama_hewan'], jenis_hewan = response['jenis_hewan'], jenis_kelamin_hewan = response['jenis_kelamin_hewan'], usia_hewan = response['usia_hewan'], domisili_hewan = response['domisili_hewan'], keterangan = response['keterangan'], kategori = response['kategori'], kondisi_kesehatan = response['kondisi_kesehatan'], lokasi_perawatan = response['lokasi_perawatan'], biaya_perawatan = response['biaya_perawatan'], verifikasi = response['verifikasi'] )
        data.save()
        return berhasil_unggah(request)
    else :    
        args = {'donasi': donasi}
        return render(request, 'opendonasi/form-eval-open-donasi.html', args)

def delete_open_donasi(request, id):
    donasi = Donasi.objects.get(id = id)
    donasi.delete()
    return redirect('/admin-adopet/')

def eval_artikel(request, id):
    artikel = Artikel.objects.get(id = id)
    if request.method == 'POST':
        response['judul_artikel'] = artikel.judul_artikel
        response['isi_artikel'] = artikel.isi_artikel
        response['tag_artikel'] = artikel.tag_artikel
        response['verifikasi_artikel'] = True
        data = Artikel(id = id, judul_artikel = response['judul_artikel'], isi_artikel = response['isi_artikel'], tag_artikel = response['tag_artikel'], verifikasi_artikel = response['verifikasi_artikel'])
        data.save()
        return berhasil_unggah(request)
    else :    
        args = {'artikel': artikel}
        return render(request, 'artikel/form-eval-artikel.html', args)
    
def delete_artikel(request, id):
    artikel = Artikel.objects.get(id = id)
    artikel.delete()
    return redirect('/admin-adopet/')

def berhasil_unggah(request):
    return render(request, 'warning/berhasil-unggah-donasi.html')

def search(request):
    searchkey = request.GET.get('search')
    database = Donasi.objects.filter(nama_hewan__icontains = searchkey)
    artikel = Artikel.objects.filter(judul_artikel__icontains = searchkey)
    context = {
        'database' : database,
        'artikel' : artikel
    }
    return render(request, 'homepage/beranda-admin.html', context)
