from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.http import JsonResponse
from django.conf import settings
import copy

from .forms import FormAdopt, FormFoto, FormRequestAdopsi, FormDonasi
from .models import Hewan, FotoHewan, RequestAdopsi, Donasi

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
	hewan = Hewan.objects.get(id = id)
	args = {'hewan' : hewan}
	return render(request, 'openadopt/detail-open-adopt.html', args)

def beranda(request):
    database = Hewan.objects.all().values()
    context = {
        'database' : database
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
        response['nama_hewan'] = hewan.nama_hewan
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
        context = {
            'form' : form 
            'pengadopsian' : pengadopsian
        }
        return render(request, 'openadopt/detail-pengadopsian.html', context)
    else:
        hewan = Hewan.objects.get(id = id)
        form = FormRequestAdopsi()
        context = {
            'form' : form,
            'hewan' : hewan
        }
        return render(request, 'openadopt/form-pengadopsian.html', context)

def detail_pengadopsian(request, id):
    database = RequestAdopsi.objects.all().values()
    context = {
        'database' : database
    }
    return render(request, 'openadopt/detail-pengadopsian.html', context)

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

def detail_donasi(request):
    return render(request, 'opendonasi/detail-open-donasi.html')
    
def melakukan_donasi(request):
    return render(request, 'opendonasi/melakukandonasi.html')

def profil(request):
    return render(request, 'profil/profil.html')

def form_request_artikel(request):
    return render(request, 'artikel/form-request-artikel.html')

def detail_artikel(request):
    return render(request, 'artikel/detailartikel.html')

def berhasil_request(request):
    return render(request, 'warning/berhasil-request.html')

def berhasil_unggah(request):
    return render(request, 'warning/berhasil-unggah.html')

def buat_testimoni(request):
    return render(request, 'profil/form-testimoni.html')

def forum(request):
    return render(request, 'forum/forum.html')
    
def chatpage(request):
    return render(request, 'chatting/chatpage.html')
