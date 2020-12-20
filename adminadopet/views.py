from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.http import JsonResponse
from django.conf import settings
import copy
from user.forms import FormDonasi
from user.models import Donasi

# Create your views here.
def beranda(request):
    database = Donasi.objects.all().values()
    context = {
        'database' : database
    }
    return render(request, 'homepage/beranda-admin.html', context)

def eval_open_donasi(request, id):
    donasi = Donasi.objects.get(id = id)
    args = {'donasi': donasi}
    return render(request, 'opendonasi/form-eval-open-donasi.html', args)

def eval_artikel(request):
    return render(request, 'artikel/form-eval-artikel.html')
 
def berhasil_unggah(request):
    return render(request, 'warning/berhasil-unggah-donasi.html')