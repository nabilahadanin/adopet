from django.shortcuts import render

# Create your views here.
def beranda(request):
    return render(request, 'homepage/beranda-admin.html')
    
def eval_open_donasi(request):
    return render(request, 'opendonasi/form-eval-open-donasi.html')