from django.shortcuts import render

# Create your views here.
def form_request_open_donasi(request):
    return render(request, 'opendonasi/form-request-open-donasi.html')

def form_open_adopt(request):
    return render(request, 'openadopt/form-open-adopt.html')

def profil(request):
    return render(request, 'profil/profil.html')

def buat_artikel(request):
    return render(request, 'artikel/buat-artikel.html')

def beranda(request):
    return render(request, 'homepage/beranda.html')

def berhasil_request(request):
    return render(request, 'warning/berhasil-request.html')

def berhasil_unggah(request):
    return render(request, 'warning/berhasil-unggah.html')