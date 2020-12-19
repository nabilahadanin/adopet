from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.http import JsonResponse
from django.conf import settings
import copy

from .forms import FormAdopt, FormFoto
from .models import Hewan, FotoHewan

def form_open_adopt(request):
    if request.method == 'POST':
        unggah_baru = copy.deepcopy(request.POST)
        form_adopt = FormAdopt(unggah_baru)
        form_foto = FormFoto(request.POST, request.FILES)
        if form_adopt.is_valid() and form_foto.is_valid():
            hewan_baru = form_adopt.save()
            foto_baru = FotoHewan(hewan = hewan_baru, foto = form_foto.cleaned_data['foto'])
            foto_baru.save()
            print("test sukses")
            return render(request, 'openadopt/form-open-adopt.html', {
                'success': True
            })
        return render(request, 'openadopt/form-open-adopt.html', {
            'failed': True
        })
    return render(request, 'openadopt/form-open-adopt.html')

def beranda(request):
    return render(request, 'homepage/beranda.html')

def list_hewan(request):
    hewan_list = list(Hewan.objects.values())
    return JsonResponse(hewan_list, safe=False)

def list_foto(request):
    foto_list = list(FotoHewan.objects.values())
    for i in range(len(foto_list)):
        photo_list[i]['foto'] = settings.MEDIA_URL + foto_list[i]['foto']
    return JsonResponse(foto_list, safe=False)


def form_request_open_donasi(request):
    return render(request, 'opendonasi/form-request-open-donasi.html')

def detail_donasi(request):
    return render(request, 'opendonasi/detail-open-donasi.html')

def melakukan_donasi(request):
    return render(request, 'opendonasi/melakukandonasi.html')

def detail_open_adopt(request):
    return render(request, 'openadopt/detail-open-adopt.html')

def form_pengadopsian(request):
    return render(request, 'openadopt/form-pengadopsian.html')

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
