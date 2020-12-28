from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.http import JsonResponse
from django.conf import settings
import copy

from user.forms import FormAdopt, FormFoto, FormRequestAdopsi, FormDonasi, FormRequestArtikel, FormTestimoni, FormForum, FormPendonasian, FormReply
from user.models import Hewan, FotoHewan, RequestAdopsi, Donasi, Artikel, Testimoni, Forum, Pendonasian, ReplyForum
from adminadopet.models import PostDonasi

# Create your views here.
def beranda_unlog(request):
    database = Hewan.objects.all().values()
    donasi = Donasi.objects.all().values()
    artikel = Artikel.objects.all().values()
    context = {
        'database' : database, 
        'donasi' : donasi,
        'artikel' : artikel
    }
    return render(request, 'homepage/beranda-unlog.html', context)

def login(request):
    return render(request, 'login/login.html')

def login_admin(request):
    return render(request, 'login/login-admin.html')
