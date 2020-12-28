from django.urls import path
from . import views

app_name = 'homepage'

urlpatterns = [
    path('', views.beranda_unlog, name='beranda_unlog'),
    path('login/', views.login, name='login'),
    path('login-admin/', views.login_admin, name='login_admin'),
]