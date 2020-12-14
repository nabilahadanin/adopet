from django.shortcuts import render

# Create your views here.
def beranda_unlog(request):
    return render(request, 'homepage/beranda-unlog.html')

def login(request):
    return render(request, 'login/login.html')

def login_admin(request):
    return render(request, 'login/login-admin.html')
