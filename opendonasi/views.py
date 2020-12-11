from django.shortcuts import render

# Create your views here.
def form_request_open_donasi(request):
    return render(request, 'opendonasi/form-request-open-donasi.html')
